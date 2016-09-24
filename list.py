# coding: utf-8
from cell import *

class List(Cell):

    def __init__(self):
        self.root = Cell()

    def get_list(self):
        print self.root.cell

    def get_each(self):
        pass

'''
    def set_list(self, *args):
        for arg in args:
            if self.root.cell == []:
                self.root = cons(arg)
            else:
                self.root = cons(arg, self.root.cell)

def set_list(*args):
    argv = list(args)
    root = None
    root = cons(argv.pop(0), root)
    set_list(argv)

print set_list(1, 2, 3)
'''
