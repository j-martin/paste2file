#!/usr/bin/env python

"""tests.py: Testing for paste2file
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

from p2f import *
from os import unlink
from time import clock


def test_init():
    test = paste2file()
    expected = 'paste2file.p2f'

    result = test.__module__

    print result
    assert (result == expected)


def test_validation():
    test = paste2file()

    inputs_list = [
        {'input': 'test.txt', },
        {'input': 'test//.txt', 'expected': False},
        {'input': 'tes-"t.txt.txt', 'expected': False},
        {'input': 't|e&st.txt', 'expected': False, },
        {'input': '', 'expected': 'clipboard.txt', },
    ]

    for inputs_dict in inputs_list:

        inputs = inputs_dict['input']
        try:
            expected = inputs_dict['expected']
        except KeyError:
            expected = inputs_dict['input']

        print('%s => %s ?' % (inputs, expected))
        result = test.set_filename(inputs)
        print(result)

        assert(result == expected)


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

    print("%r == %r ?" % (expected, result))
    unlink(filename)
    assert(expected + '\n' == result)
