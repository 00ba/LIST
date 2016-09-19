# coding: utf-8

class Cell:

    def __init__(self):
        self.cell = []

    def car(self):
        result = self.cell.pop(0)
        return result

    def cdr(self):
        result = self.cell.pop()
        return result

def cons(a, b = None):
    newcell = Cell()
    newcell.cell.insert(0, a)
    newcell.cell.append(b)
    return newcell

def atom(a):
    if isinstance(a, int):
        return True
    elif isinstance(a, str):
        return True
    else:
        False

def eq(a, b):
    if a == b:
        return True
    else:
        return False
