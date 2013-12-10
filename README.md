# paste2file


Small Python utility that copy the clipboard to a file. Can be useful when following a tutorial for example. Coded to work on Windows, *nix and OS X. This is a shell utility.

It is a quicker alternative (shorter) to pbpaste (on OS X) and works everywhere.

## Setup

1. Symlink the file p2f.py to a PATH directory as p2f (e.g. configure "ln p2f.py %HOME/bin/p2f", if you have a %HOME/bin).
1. Allow the script to be executed "chmod 755 p2f.py"

## Usage

1. Copy something in the clipboard.
1. In the terminal typing "p2f" you will be prompted to enter a filename. If you type nothing. It will dump the clipboard to the file 'clipboard.txt'.
1. Alternatively you can type "p2f <filename>" where "<filename>" is your filename (really!).

