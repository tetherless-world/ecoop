
![StickyLogo](http://tw.rpi.edu/img_projects/ECOOP-logo.png)


ECO-OP
=====

The ECO-OP project was a collaboration between computer scientists,  fisheries scientists, and oceanographers to facilitate the deployment of  an Integrated Ecosystem Approach (IEA) to management of Large Marine  Ecosystems (LMEs). Here we provide the ECO-OP software library that we  developed from a Use Case for the Ecosystem Status Report for the U.S.  Northeast Shelf Large Marine Ecosystem (LME). We focus on the Climate  Forcing chapter of this report and build a PDF document that reports on  two climate indicators. The workflow is conducted within an IPython  Notebook. The general utility of this software package is to enable the  reproducibility of a scientific workflow that acquires data online,  processes and plots data, packages text and figures into a document, and  tracks provenance of derived data and the output document. The ECO-OP  project was a collaboration between Rensselaer Polytechnic  Institute, Woods Hole Oceanographic Institution, and NOAA's Northeast  Fisheries Science Center, funded in 2010-2014 by the U.S. National Science Foundation #0955649.

---

Notebook used for the  Climate forcing UseCase :


- [clean](http://nbviewer.ipython.org/github/epifanio/ecoop-1/blob/master/pyecoop/notebook/ESR_Test.ipynb)

- [executed](http://nbviewer.ipython.org/github/epifanio/ecoop-1/blob/master/pyecoop/notebook/ESR_Test_executed.ipynb)

- [API documentation](http://ecoop.tw.rpi.edu/)

--- 

INSTALLATION:

* Download and install the ecoop code and its dependencies
    
    ```
    git clone https://github.com/tetherless-world/ecoop
    cd ecoop/pyecoop
    pip install -r requirement.txt
    python setup.py install
    ```

*  pdflatex<br>

    ```
    apt-get install texlive texlive-latex-extra      
    ```
      
* gist utility:

    ```
    apt-get install rubygems
    gem install gist
    ```
