# /usr/bin/env python
# -*- coding: utf-8 -*-

# ##############################################################################
#
#
# Project: ECOOP, sponsored by The National Science Foundation
# Purpose: this code is part of the Cyberinfrastructure developed for the ECOOP project
# http://tw.rpi.edu/web/project/ECOOP
#                from the TWC - Tetherless World Constellation
#                            at RPI - Rensselaer Polytechnic Institute
#                            founded by NSF
#
# Author:   Massimo Di Stefano , distem@rpi.edu -
#                http://tw.rpi.edu/web/person/MassimoDiStefano
#
###############################################################################
# Copyright (c) 2008-2014 Tetherless World Constellation at Rensselaer Polytechnic Institute
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
###############################################################################


from __future__ import print_function
import os
import envoy

from datetime import datetime
import numpy as np
import scipy.stats as sts
import statsmodels.api as sm
from scipy.interpolate import interp1d
import pandas as pd
import matplotlib.pyplot as plt
from ecoop.ecooputil import shareUtil as EU

lowess = sm.nonparametric.lowess

try:
    from IPython.core.display import display
except:
    print('you need to run this code from inside an IPython notebook in order to save provenance')
eu = EU()

from bokeh import pyplot


class cfData():
    def __init__(self):
        self.x = ''

    def nao_get(self,
                url="https://climatedataguide.ucar.edu/sites/default/files/climate_index_files/nao_station_djfm.txt",
                save=None, csvout='nao.csv', prov=False):
        """
        
        read NAO data from url and return a pandas dataframe
        
        :param str url: url to data online default is set to :
                    https://climatedataguide.ucar.edu/sites/default/files/climate_index_files/nao_station_djfm.txt
        :param str save: directory where to save raw data as csv
        :return: naodata as pandas dataframe
        :rtype: pandas dataframe
        
        """
        #source_code_link = "http://epinux.com/shared/pyecoop_doc/ecoop.html#ecoop.cf.cfData.nao_get"
        try:
            naodata = pd.read_csv(url, sep='  ', header=0, skiprows=0, index_col=0, parse_dates=True, skip_footer=1)
            print('dataset used: %s' % url)
            if save:
                eu.ensure_dir(save)
                output = os.path.join(save, csvout)
                naodata.to_csv(output, sep=',', header=True, index=True, index_label='Date')
                print('nao data saved in : ' + output)
            if prov:
                jsonld = {
                    "@id": "ex:NAO_dataset",
                    "@type": ["prov:Entity", "ecoop:Dataset"],
                    "ecoop_ext:hasCode": {
                        "@id": "http://epinux.com/shared/pyecoop_doc/ecoop.html#ecoop.cf.cfData.nao_get",
                        "@type": "ecoop_ext:Code",
                        "ecoop_ext:hasFunction_src_code_link": url,
                        "ecoop_ext:hasParameter": [
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "csvout",
                                "ecoop_ext:parameter_value": csvout
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "save",
                                "ecoop_ext:parameter_value": save
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "url",
                                "ecoop_ext:parameter_value": url
                            }
                        ]
                    }
                }
                display('cell-output metadata saved', metadata={'ecoop_prov': jsonld})

            return naodata
        except IOError:
            print(
                'unable to fetch the data, check if %s is a valid address and data is conform to AMO spec, for info about data spec. see [1]' % url)
            # try cached version / history-linked-uri


    def nin_get(self, url='http://www.cpc.ncep.noaa.gov/data/indices/sstoi.indices', save=None, csvout='nin.csv',
                prov=False):
        """
        
        read NIN data from url and return a pandas dataframe
        
        :param str url: url to data online default is set to : http://www.cpc.ncep.noaa.gov/data/indices/sstoi.indices
        :param str save: directory where to save raw data as csv
        :return: nindata as pandas dataframe
        :rtype: pandas dataframe

        """
        try:
            ts_raw = pd.read_table(url, sep=' ', header=0, skiprows=0, parse_dates=[['YR', 'MON']],
                                   skipinitialspace=True,
                                   index_col=0, date_parser=parse)
            print('dataset used: %s' % url)
            ts_year_group = ts_raw.groupby(lambda x: x.year).apply(lambda sdf: sdf if len(sdf) > 11 else None)
            ts_range = pd.date_range(ts_year_group.index[0][1], ts_year_group.index[-1][1] + pd.DateOffset(months=1),
                                     freq="M")
            ts = pd.DataFrame(ts_year_group.values, index=ts_range, columns=ts_year_group.keys())
            ts_fullyears_group = ts.groupby(lambda x: x.year)
            nin_anomalies = (ts_fullyears_group.mean()['ANOM.3'] - sts.nanmean(
                ts_fullyears_group.mean()['ANOM.3'])) / sts.nanstd(ts_fullyears_group.mean()['ANOM.3'])
            nin_anomalies = pd.DataFrame(nin_anomalies.values,
                                         index=pd.to_datetime([str(x) for x in nin_anomalies.index]))
            nin_anomalies = nin_anomalies.rename(columns={'0': 'nin'})
            nin_anomalies.columns = ['nin']
            if save:
                eu.ensure_dir(save)
                output = os.path.join(save, csvout)
                nin_anomalies.to_csv(output, sep=',', header=True, index=True, index_label='Date')
                print('data saved as %s ' % output)
            if prov:
                function = {}
                function['name'] = 'nin_get'
                function['parameters'] = {}
                function['parameters']['url'] = url
                function['parameters']['save'] = save
                function['parameters']['csvout'] = csvout
                display('cell-output metadata saved', metadata={'nin_get': function})
                jsonld = {
                    "@id": "ex:NIN_dataset",
                    "@type": ["prov:Entity", "ecoop:Dataset"],
                    "ecoop_ext:hasCode": {
                        "@id": "http://epinux.com/shared/pyecoop_doc/ecoop.html#ecoop.cf.cfData.nin_get",
                        "@type": "ecoop_ext:Code",
                        "ecoop_ext:hasFunction_src_code_link": url,
                        "ecoop_ext:hasParameter": [
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "csvout",
                                "ecoop_ext:parameter_value": csvout
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "save",
                                "ecoop_ext:parameter_value": save
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "url",
                                "ecoop_ext:parameter_value": url
                            }
                        ]
                    }
                }
                display('cell-output metadata saved', metadata={'ecoop_prov': jsonld})
            return nin_anomalies
        except IOError:
            print(
                'unable to fetch the data, check if %s is a valid address and data is conform to AMO spec, for info about data spec. see [1]' % url)
            # try cached version / history-linked-uri


    def parse(self, yr, mon):
        """
        
        Convert year and month to a datatime object, day hardcoded to 2nd day of each month
        
        :param yr: year date integer or string
        :param mon: month date integer or string
        :return: datatime object (time stamp)
        :rtype: datatime
        
        """
        date = datetime(year=int(yr), day=2, month=int(mon))
        return date


    def amo_get(self, url='http://www.cdc.noaa.gov/Correlation/amon.us.long.data', save=None, csvout='amo.csv',
                prov=False):
        """
        
        read AMO data from url and return a pandas dataframe
        
        :param str url: url to data online default is set to : http://www.cdc.noaa.gov/Correlation/amon.us.long.data
        :param str save: directory where to save raw data as csv
        :return: amodata as pandas dataframe
        :rtype: pandas dataframe
        
        """
        try:
            ts_raw = pd.read_table(url, sep=' ', skiprows=1,
                                   names=['year', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct',
                                          'nov', 'dec'], skipinitialspace=True, parse_dates=True, skipfooter=4,
                                   index_col=0)
            print('dataset used: %s' % url)
            ts_raw.replace(-9.99900000e+01, np.NAN, inplace=True)
            amodata = ts_raw.mean(axis=1)
            amodata.name = "amo"
            amodata = pd.DataFrame(amodata)
            if save:
                eu.ensure_dir(save)
                output = os.path.join(save, csvout)
                amodata.to_csv(output, sep=',', header=True, index=True, index_label='Date')
                print('data saved as %s ' % output)
            if prov:
                function = {}
                function['name'] = 'amo_get'
                function['parameters'] = {}
                function['parameters']['url'] = url
                function['parameters']['save'] = save
                function['parameters']['csvout'] = csvout
                jsonld = {
                    "@id": "ex:AMO_dataset",
                    "@type": ["prov:Entity", "ecoop:Dataset"],
                    "ecoop_ext:hasCode": {
                        "@id": "http://epinux.com/shared/pyecoop_doc/ecoop.html#ecoop.cf.cfData.amo_get",
                        "@type": "ecoop_ext:Code",
                        "ecoop_ext:hasFunction_src_code_link": "http://epinux.com/shared/pyecoop_doc/ecoop.html#ecoop.cf.cfData.amo_get",
                        "ecoop_ext:hasParameter": [
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "csvout",
                                "ecoop_ext:parameter_value": csvout
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "save",
                                "ecoop_ext:parameter_value": save
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "url",
                                "ecoop_ext:parameter_value": url
                            }
                        ]
                    }
                }
                display('cell-output metadata saved', metadata={'ecoop_prov': jsonld})
            return amodata
        except:
            print(
                'unable to fetch the data, check if %s is a valid address and data is conform to AMO spec, for info about data spec. see [1]' % url)
            # try cached version / history-linked-uri


class cfPlot():
    def plot_index(self, data, name='Index',
                   nb=True, datarange=None,
                   xticks=10, xticks_fontsize=10,
                   dateformat=False, figsize=(10, 8),
                   xmargin=True, ymargin=True,
                   legend=True, smoother=None,
                   output=None, dpi=300,
                   grid=True, xlabel='Year',
                   ylabel='', title='',
                   win_size=10, win_type='boxcar',
                   center=False, std=0.1,
                   beta=0.1, power=1, width=1,
                   min_periods=None, freq=None,
                   scategory=None, frac=1. / 3, it=3, figsave=None, prov=False):
        """
        
        Function to plot the Climate Forcing indicator for the ESR 2013, it follow graphic guidlines from the past ESR
        adding functionalities like :
        several kind of smoothline with different
        
        :param data: pandas dataframe - input data
        :param name: string - name used as dataframe index
        :param nb: bolean if True the function is optimized to render the png inside a notebook
        :param datarange: list of 2 integer for mak min year
        :param xticks: integer xtick spacing default=10
        :param xticks_fontsize: integer xticks fontsize default=10
        :param dateformat: boolean if True set the xticks labels in date format
        :param figsize: tuple figure size default (10, 8)
        :param xmargin: bolean default True
        :param ymargin: bolean default True
        :param legend: bolean default True
        :param smoother: tuple (f,i)
        :param output: directory where to save output default None
        :param dpi: integer
        :param grid: bolean default True
        :param xlabel: string default 'Year'
        :param ylabel: string default ''
        :param title: string default ''
        :param win_size: integer default 10
        :param win_type: string default 'boxcar'
        :param center: bolean default False
        :param std: float default 0.1
        :param beta: float default 0.1
        :param power: integer default 1
        :param width: integer default 1
        :param min_periods: None
        :param freq: None
        :param str scategory: default 'rolling'
        :param float frac: default 0.6666666666666666 Between 0 and 1. The fraction of the data used when estimating each y-value.,
        :param int it: default 3 The number of residual-based reweightings to perform.

        """
        try:
            assert type(data) == pd.core.frame.DataFrame
            #x = data.index.year
            #y = data.values
            if datarange:
                #if datarange != None :
                mind = np.datetime64(str(datarange[0]))
                maxd = np.datetime64(str(datarange[1]))
                newdata = data.ix[mind:maxd]
                x = newdata.index.year
                y = newdata.values
            else:
                x = data.index.year
                y = data.values
            x_p = x[np.where(y >= 0)[0]]
            y_p = y[np.where(y >= 0)[0]]
            x_n = x[np.where(y < 0)[0]]
            y_n = y[np.where(y < 0)[0]]
            fig = plt.figure(figsize=figsize)
            ax1 = fig.add_subplot(111)
            ax1.bar(x_n, y_n, 0.8, facecolor='b', label=name + ' < 0')
            ax1.bar(x_p, y_p, 0.8, facecolor='r', label=name + ' > 0')
            ax1.grid(grid)
            if ylabel != '':
                ax1.set_ylabel(ylabel)
            else:
                ax1.set_ylabel(name)
            if xlabel != '':
                ax1.set_xlabel(xlabel)
            else:
                ax1.set_xlabel(xlabel)
            if title == '':
                ax1.set_title(name)
            else:
                ax1.set_title(title)
            ax1.axhline(0, color='black', lw=1.5)
            if xmargin:
                ax1.set_xmargin(0.1)
            if ymargin:
                ax1.set_xmargin(0.1)
            if legend:
                ax1.legend()
            if not figsave:
                figsave = name + '.png'
            if scategory == 'rolling':
                newy = self.rolling_smoother(data, stype=smoother, win_size=win_size, win_type=win_type, center=center,
                                             std=std,
                                             beta=beta, power=power, width=width)
                ax1.plot(newy.index.year, newy.values, lw=3, color='g')
            if scategory == 'expanding':
                newy = self.expanding_smoother(data, stype=smoother, min_periods=min_periods, freq=freq)
                ax1.plot(newy.index.year, newy.values, lw=3, color='g')
            if scategory == 'lowess':
                x = np.array(range(0, len(data.index.values))).T
                newy = pd.Series(lowess(data.values.flatten(), x, frac=frac, it=it).T[1], index=data.index)
                ax1.plot(newy.index.year, newy, lw=3, color='g')
                ## interp 1D attempt
                xx = np.linspace(min(data.index.year), max(data.index.year), len(newy))
                f = interp1d(xx, newy)
                xnew = np.linspace(min(data.index.year), max(data.index.year), len(newy) * 4)
                f2 = interp1d(xx, newy, kind='cubic')
                #xnew = np.linspace(min(data.index.values), max(data.index.values), len(newy)*2)
                ax1.plot(xx, newy, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
                ##
            if scategory == 'ewma':
                print('todo')
            plt.xticks(data.index.year[::xticks].astype('int'), data.index.year[::xticks].astype('int'),
                       fontsize=xticks_fontsize)
            plt.autoscale(enable=True, axis='both', tight=True)
            if dateformat:
                fig.autofmt_xdate(bottom=0.2, rotation=75, ha='right')
            if output:
                eu.ensure_dir(output)
                ffigsave = os.path.join(output, figsave)
                plt.savefig(ffigsave, dpi=dpi)
                print('graph saved in: %s ' % ffigsave)
                if scategory:
                    smoutput = name + '_' + scategory + '.csv'
                    if smoother:
                        smoutput = name + '_' + scategory + '_' + smoother + '.csv'
                    smoutput = os.path.join(output, smoutput)
                    if scategory == 'lowess':
                        newdataframe = data.copy(deep=True)
                        newdataframe['smooth'] = pd.Series(newy, index=data.index)
                        newdataframe.to_csv(smoutput, sep=',', header=True, index=True, index_label='Year')
                    else:
                        newy.to_csv(smoutput, sep=',', header=True, index=True, index_label='Year')
                    print(name + ' smoothed data saved in : %s ' % smoutput)
            if nb:
                fig.subplots_adjust(left=-1.0)
                fig.subplots_adjust(right=1.0)
            #plt.show()
            if prov:
                function = {}
                function['name'] = 'plot_index'
                function['parameters'] = {}
                function['parameters']['data'] = data
                function['parameters']['name'] = name
                function['parameters']['nb'] = nb
                function['parameters']['datarange'] = datarange
                function['parameters']['xticks'] = xticks
                function['parameters']['xticks_fontsize'] = xticks_fontsize
                function['parameters']['dateformat'] = dateformat
                function['parameters']['figsize'] = figsize
                function['parameters']['xmargin'] = xmargin
                function['parameters']['ymargin'] = ymargin
                function['parameters']['legend'] = legend
                function['parameters']['smoother'] = smoother
                function['parameters']['output'] = output
                function['parameters']['dpi'] = dpi
                function['parameters']['grid'] = grid
                function['parameters']['xlabel'] = xlabel
                function['parameters']['ylabel'] = ylabel
                function['parameters']['title'] = title
                function['parameters']['win_size'] = win_size
                function['parameters']['win_type'] = win_type
                function['parameters']['center'] = center
                function['parameters']['std'] = std
                function['parameters']['beta'] = beta
                function['parameters']['power'] = power
                function['parameters']['width'] = width
                function['parameters']['min_periods'] = min_periods
                function['parameters']['freq'] = freq
                function['parameters']['scategory'] = scategory
                function['parameters']['frac'] = frac
                function['parameters']['it'] = it
                function['parameters']['figsave'] = figsave
                jsonld = {
                    "@id": "ex:NAO_figure",
                    "@type": ["prov:Entity", "ecoop:Figure"],
                    "ecoop_ext:hasData": "ecoop_data['NAO']",
                    "ecoop_ext:hasCode": {
                        "@type": "ecoop_ext:Code",
                        "ecoop_ext:hasFunction_src_code_link": "",
                        "ecoop_ext:hasParameter": [
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "beta",
                                "ecoop_ext:parameter_value": beta
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "center",
                                "ecoop_ext:parameter_value": center
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "data",
                                "ecoop_ext:parameter_value": data
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "datarange",
                                "ecoop_ext:parameter_value": datarange
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "dateformat",
                                "ecoop_ext:parameter_value": dateformat
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "dpi",
                                "ecoop_ext:parameter_value": dpi
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "figsave",
                                "ecoop_ext:parameter_value": figsave
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "figsize",
                                "ecoop_ext:parameter_value": figsize
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "frac",
                                "ecoop_ext:parameter_value": frac
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "freq",
                                "ecoop_ext:parameter_value": freq
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "grid",
                                "ecoop_ext:parameter_value": grid
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "it",
                                "ecoop_ext:parameter_value": it
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "legend",
                                "ecoop_ext:parameter_value": legend
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "min_periods",
                                "ecoop_ext:parameter_value": min_periods
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "name",
                                "ecoop_ext:parameter_value": name
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "nb",
                                "ecoop_ext:parameter_value": nb
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "output",
                                "ecoop_ext:parameter_value": output
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "power",
                                "ecoop_ext:parameter_value": power
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "scategory",
                                "ecoop_ext:parameter_value": scategory
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "smoother",
                                "ecoop_ext:parameter_value": smoother
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "std",
                                "ecoop_ext:parameter_value": std
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "title",
                                "ecoop_ext:parameter_value": title
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "width",
                                "ecoop_ext:parameter_value": width
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "win_size",
                                "ecoop_ext:parameter_value": win_size
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "win_type",
                                "ecoop_ext:parameter_value": win_type
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "xlabel",
                                "ecoop_ext:parameter_value": xlabel
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "xmargin",
                                "ecoop_ext:parameter_value": xmargin
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "xticks",
                                "ecoop_ext:parameter_value": xticks
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "xticks_fontsize",
                                "ecoop_ext:parameter_value": xticks_fontsize
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "ylabel",
                                "ecoop_ext:parameter_value": ylabel
                            },
                            {
                                "@type": "ecoop_ext:Parameter",
                                "ecoop_ext:parameter_name": "ymargin",
                                "ecoop_ext:parameter_value": ymargin
                            }
                        ]
                    },
                    "ecoop_ext:usedSoftware": [{"@id": "ex:ecoop_software"}, {"@id": "ex:ipython_software"}]
                }
                display('cell-output metadata saved', metadata={'ecoop_prov': jsonld})
            pyplot.show_bokeh(plt.gcf(), filename="subplots.html")
        except AssertionError:
            if type(data) != pd.core.frame.DataFrame:
                print('input data not compatible, it has to be of type : pandas.core.frame.DataFrame')
            print('data not loaded correctly')


    def rolling_smoother(self, data, stype='rolling_mean', win_size=10, win_type='boxcar', center=False, std=0.1,
                         beta=0.1,
                         power=1, width=1):
        """
        
        Perform a espanding smooting on the data for a complete help refer to http://pandas.pydata.org/pandas-docs/dev/computation.html
        
        :param data:
        :param stype:
        :param win_size:
        :param win_type:
        :param center:
        :param std:
        :param beta:
        :param power:
        :param width:
        :moothing types:
            ROLLING :
                rolling_count	Number of non-null observations
                rolling_sum	Sum of values
                rolling_mean	Mean of values
                rolling_median	Arithmetic median of values
                rolling_min	Minimum
                rolling_max	Maximum
                rolling_std	Unbiased standard deviation
                rolling_var	Unbiased variance
                rolling_skew	Unbiased skewness (3rd moment)
                rolling_kurt	Unbiased kurtosis (4th moment)
                rolling_window	Moving window function
                    window types:
                        boxcar
                        triang
                        blackman
                        hamming
                        bartlett
                        parzen
                        bohman
                        blackmanharris
                        nuttall
                        barthann
                        kaiser (needs beta)
                        gaussian (needs std)
                        general_gaussian (needs power, width)
                        slepian (needs width)
        
        """
        if stype == 'count':
            newy = pd.rolling_count(data, win_size)
        if stype == 'sum':
            newy = pd.rolling_sum(data, win_size)
        if stype == 'mean':
            newy = pd.rolling_mean(data, win_size)
        if stype == 'median':
            newy = pd.rolling_median(data, win_size)
        if stype == 'min':
            newy = pd.rolling_min(data, win_size)
        if stype == 'max':
            newy = pd.rolling_max(data, win_size)
        if stype == 'std':
            newy = pd.rolling_std(data, win_size)
        if stype == 'var':
            newy = pd.rolling_var(data, win_size)
        if stype == 'skew':
            newy = pd.rolling_skew(data, win_size)
        if stype == 'kurt':
            newy = pd.rolling_kurt(data, win_size)
        if stype == 'window':
            if win_type == 'kaiser':
                newy = pd.rolling_window(data, win_size, win_type, center=center, beta=beta)
            if win_type == 'gaussian':
                newy = pd.rolling_window(data, win_size, win_type, center=center, std=std)
            if win_type == 'general_gaussian':
                newy = pd.rolling_window(data, win_size, win_type, center=center, power=power, width=width)
            else:
                newy = pd.rolling_window(data, win_size, win_type, center=center)
        return newy


    def expanding_smoother(self, data, stype='rolling_mean', min_periods=None, freq=None):
        """
        
        Perform a expanding smooting on the data for a complete help refer to http://pandas.pydata.org/pandas-docs/dev/computation.html
        
        :param data: pandas dataframe input data
        :param stype: soothing type
        :param min_periods: periods
        :param freq: frequence
        smoothing types:
        expanding_count	Number of non-null observations
        expanding_sum	Sum of values
        expanding_mean	Mean of values
        expanding_median	Arithmetic median of values
        expanding_min	Minimum
        expanding_max	Maximum
        expandingg_std	Unbiased standard deviation
        expanding_var	Unbiased variance
        expanding_skew	Unbiased skewness (3rd moment)
        expanding_kurt	Unbiased kurtosis (4th moment)
        
        """
        if stype == 'count':
            newy = pd.expanding_count(data, min_periods=min_periods, freq=freq)
        if stype == 'sum':
            newy = pd.expanding_sum(data, min_periods=min_periods, freq=freq)
        if stype == 'mean':
            newy = pd.expanding_mean(data, min_periods=min_periods, freq=freq)
        if stype == 'median':
            newy = pd.expanding_median(data, min_periods=min_periods, freq=freq)
        if stype == 'min':
            newy = pd.expanding_min(data, min_periods=min_periods, freq=freq)
        if stype == 'max':
            newy = pd.expanding_max(data, min_periods=min_periods, freq=freq)
        if stype == 'std':
            newy = pd.expanding_std(data, min_periods=min_periods, freq=freq)
        if stype == 'var':
            newy = pd.expanding_var(data, min_periods=min_periods, freq=freq)
        if stype == 'skew':
            newy = pd.expanding_skew(data, min_periods=min_periods, freq=freq)
        if stype == 'kurt':
            newy = pd.expanding_kurt(data, min_periods=min_periods, freq=freq)
        return newy
