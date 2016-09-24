# coding: utf-8

from cell import *
from list import *

root = None

def foo(argv, n):
    if [] == argv:
        return n
    else:
        n = cons(argv.pop(0), n)
        foo(argv, n)


n = foo([1, 2, 3], root)
n.cell
