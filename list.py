'''
Created on Sep 8, 2016


'''

class Cell:

    def __init__(self, a, b):
        self.cell = [a, b]

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
        self.root = Cell(None, None)

    def get_list(self):
        if None is self.get_car:
            return []
        elif atom(self.get_car):
            return self.get_car
        else:
            self.get_list(self.get_cdr)

    def set_list(self, *args):
        if None is args.get_car:
            return []
        elif atom(args.get_car):
            return self.set_car(args)
        else:
            self.get_list(args.get_cdr)

def cons(a, b):
    newcell = Cell(None, None)
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
