#!/usr/bin/env python

"""p2f.py: Copies the content of the clipboard to a file.
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
            assert(self._filename != False)
        except AttributeError:
            print 'Enter the filename: '
            self._filename = self._validate_filename(silent=False)

    def _validate_filename(self, filename=None, silent=True):

        if not silent:
            filename = raw_input()

        if re.match("^[a-zA-Z0-9\._/\s]*$", filename):
            return filename
        else:

            print 'Invalid Filename. Try Again'
            if not silent:
                self._validate_filename()
            else:
                return False

    def _save_to_file(self):
        file = open(self._filename, 'w')
        file.write(self._clipboard)
        file.close()

    def do(self):
        """The method that does it all.
        """

        self._get_clipboard()
        self._prompt_for_filename()
        self._save_to_file()

if __name__ == '__main__':

    clipboard = paste2file()

    try:
        arg_filename = sys.argv[-1]
        clipboard.set_filename(arg_filename)
    except IndexError:
        pass

    clipboard.do()
