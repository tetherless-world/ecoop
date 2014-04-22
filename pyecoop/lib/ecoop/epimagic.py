# This code can be put in any Python module, it does not require IPython
# itself to be running already.  It only creates the magics subclass but
# doesn't instantiate it yet.
from __future__ import print_function

import json
import os
import io

from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)
from IPython.core import magic_arguments
from IPython.core.display import display 
from IPython.utils.py3compat import unicode_type
from IPython.utils.path import unquote_filename

class JustMetadata(object):
    def __init__(self, metadata):
        self.metadata = metadata
    
    def _repr_json_(self):
        return json.dumps(self.metadata)

@magics_class
class MyMagics(Magics):

    
    @magic_arguments.magic_arguments()
    @magic_arguments.argument(
        '-a', '--append', action='store_true', default=False,
        help='Append contents of the cell to an existing file. '
             'The file will be created if it does not exist.'
    )
    @magic_arguments.argument(
        'filename', type=unicode_type,
        help='file to write'
    )
    
    @magic_arguments.argument(
        'metadata', type=unicode_type,
        help='metadata to write'
    )
    
    @cell_magic
    def writefile2(self, line, cell):
        """Write the contents of the cell to a file.
        """
        args = magic_arguments.parse_argstring(self.writefile2, line)
        print(args)
        filename = os.path.expanduser(unquote_filename(args.filename))
        
        if os.path.exists(filename):
            print("Overwriting %s" % filename)
        else:
            print("Writing %s" % filename)
        
        mode = 'a' if args.append else 'w'
        with io.open(filename, mode, encoding='utf-8') as f:
            f.write(cell)
        

        display(metadata={'filename' : filename} )
        print(filename)


ip = get_ipython()
ip.register_magics(MyMagics)