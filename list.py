'''
Created on Sep 8, 2016


'''

class Cell:

    def __init__(self):
        self.cell = []

    def get_car(self):
        result = self.cell.pop(0)
        return result

    def set_car(self, n):
        self.cell.insert(0, n)

    def get_cdr(self):
        result = self.cell.pop()
        return result

    def set_cdr(self, n):
        self.cell.append(n)

class List(Cell):

    def __init__(self):
        self.root = Cell()

    def get_list(self):
        if None is self:
            return []
        elif atom(self.get_car):
            return self.get_car
        else:
            self.get_list(self.get_cdr)

    def set_list(self, *args):
        for arg in args:
            result = cons(arg)
            return result

def show_list(n):
    if None is n:
        print []
    elif atom(n[0]):
        print n[0]
        n = n.pop()
        show_list(n)

def cons(a, b = None):
    newcell = Cell()
    newcell.set_car(a)
    newcell.set_cdr(b)
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
