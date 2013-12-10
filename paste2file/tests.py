#!/usr/bin/env python

"""tests.py: Testing for font2css
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

from fromcpb import *
from os import unlink
from time import clock


def test_init():
    test = paste2file()

    assert (test.__module__ == 'fromcpb.fromcpb')


def test_validation():
    test = paste2file()

    print(test.set_filename('test.txt'))
    assert(test.set_filename('test.txt') != False)

    print(test.set_filename('test//.txt'))
    assert(test.set_filename('test//.txt') != False)

    print(test.set_filename('tes-"t.txt'))
    assert(test.set_filename('tes-"t.txt') == False)

    print(test.set_filename('t|e&st.txt'))
    assert(test.set_filename('t|e&st.txt') == False)


def test_get_clipboard():
    test = paste2file()

    # Fixture

    test._root.clipboard_clear()
    test._root.clipboard_append('ok')

    assert (test._get_clipboard() == 'ok')


def test_do():
    test = paste2file()

    expected = 'ok'
    filename = 'test%s' % clock()

    # Fixture
    test._root.clipboard_clear()
    test._root.clipboard_append(expected)

    test.set_filename(filename)
    test.do()

    # Check
    result = open(filename).read()
    assert(expected == result)

    # Cleanup
    unlink(filename)
