
.. code:: python

    import os
    import time
    from ecoop.ecooputil import shareUtil
    from ecoop.cf import cfData, cfPlot
    from ecoop.ecooprovdict import ecooProvDict
    from ecoop.printer import openDocument, closeDocument, addSection, addSubSection, addFigure
    from ecoop.splashtemplate import makeSplash
    from ecoop.splashdict import splash
    from ecoop.epimagic import *
.. code:: python

    #ecooProvDict
.. code:: python

    %matplotlib inline
.. code:: python

    util = shareUtil()
    cfd = cfData()
    cfp = cfPlot()
Document
========

.. code:: python

    ID = util.get_id('test/Climate-forcing_pdf')
    document = openDocument()

.. parsed-literal::

    session data directory : test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM


Section 1
---------

.. code:: python

    %%writefileref {ID}/climate_forcing.txt epinux
    Climate patterns over the North Atlantic are important drivers of oceanographic conditions and ecosystem states. 
    Steadily increasing atmospheric carbon dioxide levels can not only affect climate on global and regional scales 
    but alter critical aspects of ocean chemistry. Here, we describe the atmospheric forcing mechanisms related 
    to climate in this region including large-scale atmospheric pressure systems, natural ocean temperature cycles in the North Atlantic, 
    components of the large-scale circulation of the Atlantic Ocean, and issues related to ocean acidification.

.. parsed-literal::

    Writing test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/climate_forcing.txt



.. parsed-literal::

    'added references for user epinux'


.. code:: python

    section = addSection(name='Climate Forcing', data=os.path.join(ID,'climate_forcing.txt'))  
Sub Section 1
~~~~~~~~~~~~~

.. code:: python

    %%writefileref {ID}/nao.txt epinux
    Climate and weather over the North Atlantic are strongly influenced by the relative strengths 
    of two large-scale atmospheric pressure cells -- the Icelandic Low and the Azores High [4]. 
    As the relative strengths of these two pressure systems vary, characteristic patterns of temperature, precipitation, and wind fields are observed. 
    An index of this dipole pattern has been developed based on the standardized difference in sea level pressure between Lisbon, Portugal and Reykjavík, 
    Iceland in the winter (December-February; see Glossary for a description of methods used to create standardized indicators). 
    This North Atlantic Oscillation (NAO) index has been related to key oceanographic and ecological processes in the North Atlantic basin [5].  
    When the NAO index is high (positive NAO state), the westerly winds shift northward and increase in strength. 
    Additionally, there is an increase in precipitation over southeastern Canada, the eastern seaboard of the United States, 
    and northwestern Europe. Water temperatures are cool off Labrador and northern Newfoundland, influencing the formation of Deep Labrador Slope water, 
    but warm off the United States. 
    Conversely, when the NAO index is low (negative NAO state), there is a southward shift and decrease in westerly winds, decreased storminess, 
    and drier conditions over southeastern Canada, the eastern United States, and northwestern Europe. 
    Water temperatures are warmer off Labrador and Newfoundland, but cooler off the eastern United States. 
    Since 1972, the NAO has primarily been in a positive state (Figure 1), although notable short-term reversals to a negative state have been observed during this period. 
    Changes in the NAO have been linked to changes in plankton community composition in the North Atlantic, reflecting changes in both the distribution 
    and abundance of warm and cold-temperate species.

.. parsed-literal::

    Writing test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/nao.txt



.. parsed-literal::

    'added references for user epinux'


.. code:: python

    naodata = cfd.nao_get(save=ID, csvout="nao.csv", prov=True)

.. parsed-literal::

    dataset used: https://climatedataguide.ucar.edu/sites/default/files/climate_index_files/nao_station_djfm.txt
    nao data saved in : test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/nao.csv



.. parsed-literal::

    'cell-output metadata saved'


.. code:: python

    # NAO
    naodata = cfd.nao_get(save=ID, csvout="nao.csv")
    cfp.plot_index(name='NAO_lowess', xticks=10, xticks_fontsize=10, 
                   data=naodata, nb='y', scategory='lowess', frac=1./6, it=6, 
                   output=ID, dateformat=True, figsave="nao.png", prov=True)

.. parsed-literal::

    dataset used: https://climatedataguide.ucar.edu/sites/default/files/climate_index_files/nao_station_djfm.txt
    nao data saved in : test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/nao.csv
    graph saved in: test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/nao.png 
    NAO_lowess smoothed data saved in : test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/NAO_lowess_lowess.csv 



.. parsed-literal::

    'cell-output metadata saved'


.. parsed-literal::

    Session output file 'subplots.html' already exists, will be overwritten.



.. image:: output_12_3.png


.. code:: python

    #from bokeh import pyplot
.. code:: python

    time.sleep(1)
    nb_name = 'ESR_Test_rdf.ipynb'
    util.save_notebook(ID, nb_name)
    time.sleep(1)
    
    !rm -rf splash_nao.ipynb
    
    nao_datafile = os.path.join(ID,'nao.csv')
    naodatalink = util.gistit(filename=nao_datafile, jist='/usr/local/bin/gist', type='text')
    nbviewerlink = util.gistit(filename=nb_name, jist='/usr/local/bin/gist', type='notebook')
    
    splash['NAO']['nbviewer'] = nbviewerlink
    splash['NAO']['repository'] = 'https://github.com/epifanio/ecoop'
    splash['NAO']['download'] = 'http://144.76.93.231/shared/%s' % ID
    
    f = open('splash_nao.ipynb', 'w')
    f.write(makeSplash(splash, 'NAO'))
    f.close()
    naosplashlink = util.gistit(filename='splash_nao.ipynb', jist='/usr/local/bin/gist', type='notebook')
    
    naofig = addFigure(img=os.path.join(ID,'nao.png'), name='North Atlantic Oscillation', metadata=naosplashlink)


.. parsed-literal::

    <IPython.core.display.Javascript object>


.. parsed-literal::

    input file ESR_Test_rdf.ipynb not found


.. code:: python

    naosubsection = addSubSection(name='North Atlantic Oscillation Index', data=os.path.join(ID,'nao.txt'), fig=naofig)
Sub Section 2
~~~~~~~~~~~~~

.. code:: python

    %%writefileref {ID}/amo.txt epinux
    Multidecadal patterns in sea surface temperature (SST) in the North Atlantic are represented by the Atlantic Multidecadal Oscillation (AMO) index. 
    The AMO signal is based on spatial patterns in SST variability after removing the effects of anthropogenic forcing on temperature, 
    revealing natural long term cycles in SST.
    The AMO is characterized by warm and cool phases [6] with periods of approximately 20-40 years. 
    The AMO index is related to air temperatures and rainfall over North America and Europe and is associated 
    with changes in the frequency of droughts in North America and the frequency of severe hurricane events. 
    The AMO is thought to be related to the North Atlantic branch of the deep thermohaline circulation 
    (for more see The Gulf Stream below) which is in turn directly related to dynamics of the Gulf Stream.
    The AMO index shows a relatively cool period starting in the early 1960s, extending through the mid 1990s. 
    Since 1997, the AMO has been in a warm phase (Figure 2). 
    If past patterns continue to hold, the warm phase will potentially continue for the next several decades.

.. parsed-literal::

    Writing test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/amo.txt



.. parsed-literal::

    'added references for user epinux'


.. code:: python

    # AMO
    amodata = cfd.amo_get(save=ID, csvout="amo.csv")
    cfp.plot_index(name='AMO_lowess', xticks=10, xticks_fontsize=10, 
                   data=amodata, nb='y', scategory='lowess', frac=1./6, it=6, 
                   output=ID, dateformat=True, figsave="amo.png", prov=True)

.. parsed-literal::

    dataset used: http://www.cdc.noaa.gov/Correlation/amon.us.long.data
    data saved as test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/amo.csv 
    graph saved in: test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/amo.png 
    AMO_lowess smoothed data saved in : test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/AMO_lowess_lowess.csv 



.. parsed-literal::

    'cell-output metadata saved'


.. parsed-literal::

    Session output file 'subplots.html' already exists, will be overwritten.



.. image:: output_18_3.png


.. code:: python

    time.sleep(1)
    nb_name = 'ESR_Test_rdf.ipynb'
    util.save_notebook(ID, nb_name)
    time.sleep(1)
    
    amo_datafile = os.path.join(ID,'amo.csv')
    amodatalink = util.gistit(filename=amo_datafile, jist='/usr/local/bin/gist', type='text')
    nbviewerlink2 = util.gistit(filename=nb_name, jist='/usr/local/bin/gist', type='notebook')
    
    splash['AMO']['nbviewer'] = nbviewerlink
    splash['AMO']['repository'] = 'https://github.com/epifanio/ecoop'
    splash['AMO']['download'] = 'http://144.76.93.231/shared/%s' % ID
    
    f = open('splash_amo.ipynb', 'w')
    f.write(makeSplash(splash, 'AMO'))
    f.close()
    amosplashlink = util.gistit(filename='splash_amo.ipynb', jist='/usr/local/bin/gist', type='notebook')
    
    amofig = addFigure(img=os.path.join(ID,'amo.png'), name='Atlantic Multidecadal Oscillation', metadata=amosplashlink)


.. parsed-literal::

    <IPython.core.display.Javascript object>


.. parsed-literal::

    input file ESR_Test_rdf.ipynb not found


.. code:: python

    amosubsection = addSubSection(name='Atlantic Multidecadal Oscillation', data=os.path.join(ID,'amo.txt'), fig=amofig)
Write Document
==============

.. code:: python

    closedDocument = closeDocument()
.. code:: python

    texfile=''
    texfile += document
    texfile += section
    texfile += naosubsection
    texfile += amosubsection
    texfile += closedDocument
.. code:: python

    #print texfile
.. code:: python

    pdf = os.path.join(ID,'test.tex')
    f = open(pdf,'w')
    f.write(texfile)
    f.close()
.. code:: python

    !pdflatex -output-directory={ID} {pdf}

.. parsed-literal::

    This is pdfTeX, Version 3.1415926-2.4-1.40.13 (TeX Live 2012/Debian)
     restricted \write18 enabled.
    entering extended mode
    (./test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/test.tex
    LaTeX2e <2011/06/27>
    Babel <v3.8m> and hyphenation patterns for english, dumylang, nohyphenation, et
    hiopic, farsi, arabic, pinyin, croatian, bulgarian, ukrainian, russian, slovak,
     czech, danish, dutch, usenglishmax, ukenglish, finnish, french, basque, ngerma
    n, german, swissgerman, ngerman-x-2012-05-30, german-x-2012-05-30, monogreek, g
    reek, ibycus, ancientgreek, hungarian, bengali, tamil, hindi, telugu, gujarati,
     sanskrit, malayalam, kannada, assamese, marathi, oriya, panjabi, italian, lati
    n, latvian, lithuanian, mongolian, mongolianlmc, nynorsk, bokmal, indonesian, e
    speranto, coptic, welsh, irish, interlingua, serbian, serbianc, slovenian, friu
    lan, romansh, estonian, romanian, armenian, uppersorbian, turkish, afrikaans, i
    celandic, kurmanji, polish, portuguese, galician, catalan, spanish, swedish, th
    ai, loaded.
    (/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
    Document Class: article 2007/10/19 v1.4h Standard LaTeX document class
    (/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))
    (/usr/share/texlive/texmf-dist/tex/latex/tools/multicol.sty)
    (/var/lib/texmf/tex/generic/babel/babel.sty
    (/usr/share/texlive/texmf-dist/tex/generic/babel/english.ldf
    (/usr/share/texlive/texmf-dist/tex/generic/babel/babel.def)))
    (/usr/share/texlive/texmf-dist/tex/latex/blindtext/blindtext.sty
    (/usr/share/texlive/texmf-dist/tex/latex/tools/xspace.sty))
    (/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
    (/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
    (/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
    (/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
    (/usr/share/texlive/texmf-dist/tex/latex/latexconfig/graphics.cfg)
    (/usr/share/texlive/texmf-dist/tex/latex/pdftex-def/pdftex.def
    (/usr/share/texlive/texmf-dist/tex/generic/oberdiek/infwarerr.sty)
    (/usr/share/texlive/texmf-dist/tex/generic/oberdiek/ltxcmds.sty))))
    (/usr/share/texlive/texmf-dist/tex/latex/wrapfig/wrapfig.sty)
    (/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
    (/usr/share/texlive/texmf-dist/tex/generic/oberdiek/hobsub-hyperref.sty
    (/usr/share/texlive/texmf-dist/tex/generic/oberdiek/hobsub-generic.sty))
    (/usr/share/texlive/texmf-dist/tex/generic/ifxetex/ifxetex.sty)
    (/usr/share/texlive/texmf-dist/tex/latex/oberdiek/kvoptions.sty)
    (/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)
    (/usr/share/texlive/texmf-dist/tex/latex/latexconfig/hyperref.cfg)
    (/usr/share/texlive/texmf-dist/tex/latex/url/url.sty))
    
    Package hyperref Message: Driver (autodetected): hpdftex.
    
    (/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
    (/usr/share/texlive/texmf-dist/tex/latex/oberdiek/rerunfilecheck.sty))
    (/usr/share/texlive/texmf-dist/tex/latex/fancyvrb/fancyvrb.sty
    Style option: `fancyvrb' v2.7a, with DG/SPQR fixes, and firstline=lastline fix 
    <2008/02/07> (tvz)) (/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty
    (/usr/share/texlive/texmf-dist/tex/latex/base/utf8.def
    (/usr/share/texlive/texmf-dist/tex/latex/base/t1enc.dfu)
    (/usr/share/texlive/texmf-dist/tex/latex/base/ot1enc.dfu)
    (/usr/share/texlive/texmf-dist/tex/latex/base/omsenc.dfu)))
    No file test.aux.
    (/usr/share/texlive/texmf-dist/tex/context/base/supp-pdf.mkii
    [Loading MPS to PDF converter (version 2006.09.02).]
    ) (/usr/share/texlive/texmf-dist/tex/latex/oberdiek/epstopdf-base.sty
    (/usr/share/texlive/texmf-dist/tex/latex/oberdiek/grfext.sty)
    (/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
    (/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty
    (/usr/share/texlive/texmf-dist/tex/generic/oberdiek/gettitlestring.sty))
    (./test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/climate_forcing.
    txt)
    Overfull \hbox (5.86142pt too wide) in paragraph at lines 1--15
    \OT1/cmr/m/n/10 graphic con-di-tions and ecosys-tem states.
    
    Overfull \hbox (0.47256pt too wide) in paragraph at lines 1--15
    \OT1/cmr/m/n/10 Steadily in-creas-ing at-mo-spheric car-bon
    
    Overfull \hbox (2.1947pt too wide) in paragraph at lines 1--15
    \OT1/cmr/m/n/10 al-ter crit-i-cal as-pects of ocean chem-istry.
    
    Overfull \hbox (0.16687pt too wide) in paragraph at lines 1--15
    \OT1/cmr/m/n/10 Here, we de-scribe the at-mo-spheric forc-
    
    Overfull \hbox (0.9447pt too wide) in paragraph at lines 1--15
    \OT1/cmr/m/n/10 spheric pres-sure sys-tems, nat-u-ral ocean
    (./test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/nao.txt)
    <test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/nao.png, id=4, 722
    .7pt x 578.16pt>
    <use test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/nao.png>
    Overfull \hbox (3.21652pt too wide) in paragraph at lines 19--20
    [][] 
    
    Overfull \hbox (4.58365pt too wide) in paragraph at lines 1--22
    \OT1/cmr/m/n/10 dipole pat-tern has been de-vel-oped based
    
    Overfull \hbox (5.44257pt too wide) in paragraph at lines 1--22
    \OT1/cmr/m/n/10 NAO in-dex is high (pos-i-tive NAO state),
    
    Overfull \hbox (3.93552pt too wide) in paragraph at lines 1--22
    \OT1/cmr/m/n/10 in-crease in strength. Ad-di-tion-ally, there
    
    Overfull \hbox (6.91693pt too wide) in paragraph at lines 1--22
    \OT1/cmr/m/n/10 is an in-crease in pre-cip-i-ta-tion over south-
    
    Overfull \hbox (7.66698pt too wide) in paragraph at lines 1--22
    \OT1/cmr/m/n/10 south-east-ern Canada, the east-ern United
    
    Overfull \hbox (10.41696pt too wide) in paragraph at lines 1--22
    \OT1/cmr/m/n/10 ter tem-per-a-tures are warmer off Labrador
    
    Overfull \hbox (4.97258pt too wide) in paragraph at lines 1--22
    \OT1/cmr/m/n/10 state (Fig-ure 1), al-though no-table short-
    
    Overfull \hbox (15.43553pt too wide) in paragraph at lines 1--22
    \OT1/cmr/m/n/10 been ob-served dur-ing this pe-riod. Changes
    
    Overfull \hbox (1.4436pt too wide) in paragraph at lines 1--22
    \OT1/cmr/m/n/10 in the NAO have been linked to changes
    
    Overfull \hbox (13.81111pt too wide) in paragraph at lines 23--23
    []\OT1/cmr/bx/n/12 Atlantic Mul-ti-decadal Os-
    (./test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/amo.txt)
    <test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/amo.png, id=8, 722
    .7pt x 578.16pt>
    <use test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/amo.png>
    Overfull \hbox (3.21652pt too wide) in paragraph at lines 26--27
    [][] 
    
    Overfull \hbox (8.83362pt too wide) in paragraph at lines 1--29
    \OT1/cmr/m/n/10 Multidecadal pat-terns in sea sur-face tem-
    [1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map} <./test/Climate-forcing_p
    df_Thursday_24_April_2014_05_25_09_PM/nao.png>] [2 <./test/Climate-forcing_pdf_
    Thursday_24_April_2014_05_25_09_PM/amo.png>]
    (test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/test.aux) )
    (see the transcript file for additional information)</usr/share/texlive/texmf-d
    ist/fonts/type1/public/amsfonts/cm/cmbx12.pfb></usr/share/texlive/texmf-dist/fo
    nts/type1/public/amsfonts/cm/cmr10.pfb>
    Output written on test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_PM/t
    est.pdf (2 pages, 515875 bytes).
    Transcript written on test/Climate-forcing_pdf_Thursday_24_April_2014_05_25_09_
    PM/test.log.


.. code:: python

    !rm -rf /var/www/shared/test.pdf
.. code:: python

    !cp {ID}/test.pdf /var/www/shared/test.pdf
PDF available at http://www.epinux.com/shared/test.pdf

or via QR code :

.. code:: python

    from IPython.core.display import Image
    !rm -rf pdf.png
    import qrcode
    img = qrcode.make("http://144.76.93.231/shared/test.pdf")
    img.save("pdf.png")
    Image('pdf.png')



.. image:: output_31_0.png



Upload to SFTP :

``from secret import username, password, hostname, port inputfile = ID outputfile = '/var/www/shared/%s.zip' % ID util.uploadfile(username=username,                  password=password,                  hostname=hostname,                  port=port,                  inputfile=inputfile,                 outputfile=outputfile,                  zip=True, link=True, qr=True, apacheroot='/var/www/')``

-  User and Version Info

.. code:: python

    import getpass
    user = getpass.getuser()
    from ecoop import version
    from ecoop.userdict import ecoopuser
.. code:: python

    git_revision = version.git_revision
    short_version= version.short_version
    author = ecoopuser[user]
.. code:: python

    git_revision, short_version



.. parsed-literal::

    ('4860db2973aca305fca52d1a4e2540bbf1643e24', '0.1.0')



.. code:: python

    author.keys()



.. parsed-literal::

    dict_keys(['Organization', 'subOrganization', 'mbox', 'address', 'phone', 'familyName', 'homepageURL', 'Group', 'givenName'])



.. code:: python

    author



.. parsed-literal::

    {'Organization': 'Rensselaer Polytechnic Institute',
     'subOrganization': 'Tetherless World Constellation',
     'mbox': 'distem@rpi.edu',
     'address': '22 Millfield St Woods Hole MA US',
     'phone': '0015082924078',
     'familyName': 'Di Stefano',
     'homepageURL': 'http://tw.rpi.edu/web/person/MassimoDiStefano',
     'Group': {'mbox': '',
      'address': '',
      'subgroup': '',
      'phone': '',
      'organization': '',
      'members': '',
      'homepageURL': '',
      'name': 'TWC'},
     'givenName': 'Massimo'}



INSTALLATION:

-  Download and install the ecoop code and its dependencies

   ::

       git clone https://github.com/epifanio/ecoop-1
       cd ecoop-1/pyecoop
       pip install -r requirement.txt
       python setup.py install

-  pdflatex

   ::

       apt-get install texlive texlive-latex-extra      

-  gist utility:

   ::

       apt-get install rubygems
       gem install gist
