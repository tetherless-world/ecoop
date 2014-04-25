
North Atlantic Oscillation
==========================

-  Enable inline printing
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    %matplotlib inline

-  Import the cfData, cfPlot classes from the ecoop library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from ecoop.cf import cfData, cfPlot
.. code:: python

    cfd = cfData()
    cfp = cfPlot()
-  Retrieve the North Atlantic Oscillation dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    naodata = cfd.nao_get(prov=True)

.. parsed-literal::

    dataset used: https://climatedataguide.ucar.edu/sites/default/files/climate_index_files/nao_station_djfm.txt



.. parsed-literal::

    'cell-output metadata saved'


-  Plot the North Atlantic Oscillation dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    # NAO
    naodata = cfd.nao_get()
    cfp.plot_index(name='NAO_lowess', xticks=10, xticks_fontsize=10, 
                   data=naodata, nb='y', scategory='lowess', frac=1./6, it=6, 
                   dateformat=True)

.. parsed-literal::

    dataset used: https://climatedataguide.ucar.edu/sites/default/files/climate_index_files/nao_station_djfm.txt
    Session output file 'subplots.html' already exists, will be overwritten.



.. image:: _static/output_7_3.png
     :scale: 50

