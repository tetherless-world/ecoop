import os
def openDocument(col='twocolumn'):
    '''

    return a portion of latex template to begin a document to generate a standard or twocolumns odf document

    :param str col: onecolumn or twocolumn
    :return: partial latex template
    :rtype: str

    '''
    doc = """\documentclass{article}
        \\usepackage{multicol}
        \\usepackage[english]{babel}
        \\usepackage{blindtext}
        \\usepackage[pdftex]{graphicx}
        \\usepackage{graphicx}
        \\usepackage{wrapfig}
        \\usepackage{hyperref}
        \\usepackage{fancyvrb}
        \\usepackage[utf8]{inputenc}
        \\begin{document}
        \\begin{%s}
        """ % col
    return doc
    
def closeDocument(col='twocolumn'):
    '''

    return a portion of latex template to close a document to generate a standard or twocolumns odf document

    :param str col: onecolumn or twocolumn
    :return: partial latex template
    :rtype: str

    '''
    doc = """\end{%s}
        \end{document}
        """ % (col)
    return doc

def addSection(name, data, fig=''):
    '''

    return a portion of latex template to ad section to a latex document

    :param str name: title for
    :param str data:
    :param str fig:
    :return: partial latex template
    :rtype: str

    '''
    doc = """\section{%s}
        \input{%s}
        %s
        """ % (name, data, fig)
    return doc
    
def addSubSection(name, data, fig=''):
    doc = """\subsection{%s}
        \input{%s}
        %s
        """ % (name, data, fig)
    return doc
    
def addFigure(img, name, metadata):
    doc ="""\\begin{figure}[h]
        {\includegraphics[width=60mm]{%s}}
        \caption{%s - \href{%s}{metadata}.}
        \end{figure}
        """ % (img, name, metadata)
    return doc