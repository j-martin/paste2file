#!/usr/bin/env python

"""p2f.py: Small Python utility that copy the clipboard to a file. Can be useful
when following a tutorial for example. Coded to work on Windows, *nix and OS X.
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

import Tkinter
import re
import sys
import os


class paste2file(object):

    """docstring for paste2file"""

    def __init__(self):
        self._root = Tkinter.Tk()
        self._root.withdraw()

    def set_filename(self, filename):
        """Enables the user to define the filename before the prompt"""

        filename = self._validate_filename(filename=filename)
        self._filename = filename
        return filename

    def _get_clipboard(self):
        self._clipboard = self._root.clipboard_get()
        return self._clipboard

    def _prompt_for_filename(self):

        try:
            self._filename
        except AttributeError:
            sys.stdout.write('Output Path (default: ./clipboard.txt): ')
            self._filename = self._validate_filename(silent=False)

    def _validate_filename(self, filename=None, silent=True):

        if not silent:
            filename = raw_input()

        if filename == '':
            return 'clipboard.txt'
        elif re.match("^[a-zA-Z0-9\._\s]*$", filename):
            return filename
        else:

            print 'Invalid Filename. Try Again'
            if not silent:
                self._validate_filename()
            else:
                return False

    def _save_to_file(self):

        file = open(self._filename, 'w')
        file.write(self._clipboard + '\n')
        file.close()

    def do(self):
        """The method that does it all.
        """

        self._get_clipboard()
        self._save_to_file()

if __name__ == '__main__':

    clipboard = paste2file()

    if len(sys.argv) > 1:
        clipboard.set_filename(sys.argv[1])
    else:
        clipboard._prompt_for_filename()

    clipboard.do()
