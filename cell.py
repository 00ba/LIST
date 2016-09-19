# coding: utf-8

class Cell:

    def __init__(self, a = None, b = None):
        self.cell = [a, b]

    def car(self):
        result = self.cell.pop(0)
        return result

    def cdr(self):
        result = self.cell.pop()
        return result

def cons(a, b):
    newcell = Cell(a, b)
    return newcell

def atom(a):
    if isinstance(a, int):
        return True
    elif isinstance(a, str):
        return True
    else:
        return False

def eq(a, b):
    if a == b:
        return True
    else:
        return False
