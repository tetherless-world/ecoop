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

from ecoop.userdict import ecoopuser

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
        'username', type=unicode_type,
        help='username to assign references to cell content'
    )
    
    @cell_magic
    def writefileref(self, line, cell):
        args = magic_arguments.parse_argstring(self.writefileref, line)
        filename = os.path.expanduser(unquote_filename(args.filename))
        if os.path.exists(filename):
            print("Overwriting %s" % filename)
        else:
            print("Writing %s" % filename)
        mode = 'a' if args.append else 'w'
        with io.open(filename, mode, encoding='utf-8') as f:
            f.write(cell)
        username = os.path.expanduser(args.username)
        if username in ecoopuser.keys():
            #ecoopuser[username]['attibution']=filename
            display('added references for user %s' % username, metadata={'references': ecoopuser[username]})

ip = get_ipython()
ip.register_magics(MyMagics)