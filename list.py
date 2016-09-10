'''
Created on Sep 8, 2016

@author: oobasatoshi
'''

class Cell:

    def __init__(self):
        self.cell = {'car':None, 'cdr':None}

    def get_car(self):
        return self.cell['car']

    def set_car(self, n):
        self.cell['car'] = n

    def get_cdr(self):
        return self.cell['cdr']

    def set_cdr(self, n):
        self.cell['cdr'] = n

def get_list(newcell):
    if atom(newcell.get_car):
        return newcell.get_car
    else
        get_list(newcell.get_cdr)

def cons(a, b):
    newcell = Cell()
    newcell.cell['car'] = a
    newcell.cell['cdr'] = b
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

if __name__ == '__main__':
    try:
        root = Cell()
        one = Cell()
        one.set_car(1)
        root = root.cons(2, one)
    except:
        pass
    else:
        pass
    finally:
        print get_list(one)
        print root.cell.values()
