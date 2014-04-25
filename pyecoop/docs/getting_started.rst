.. _getting_started:


***************
Getting started
***************

.. _installing-ecoop:

Installing the ecoop library
============================

Download and install the ecoop code and its dependencies::

  git clone https://github.com/tetherless-world/ecoop
  cd ecoop/pyecoop
  pip install -r requirement.txt
  python setup.py install

If not installed already add pdflatex to your system, on debian based distros run::

  apt-get install texlive texlive-latex-extra      

Now add the gist utility::

  apt-get install rubygems
  gem install gist


.. _create-an-IPython-Notebook-profile:
    
Create an IPython Notebook profile
==================================

Create a custom profile for the notebook, with the following command line, type:::


    ipython profile create ecoop


this will generate a directory :file:`.ipython/profile_ecoop` in your :file:`$HOME` ::

    
	ls .ipython/profile_ecoop
	db				log
	history.sqlite			pid
	ipython_config.py		security
	ipython_nbconvert_config.py	startup
	ipython_notebook_config.py	static


.. _configure-an-IPython-Notebook-profile:


Configure the IPython Notebook profile
======================================


	from IPython.lib import passwd
	passwd()
	Enter password:
	Verify password:
	Out[2]: 'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed'
	
You can then add this to your ipython_notebook_config.py, e.g.::


	c = get_config()
	c.NotebookApp.password =
	u'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed'


:ref:`NAO`.





