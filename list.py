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
        
class List:
        
    def get_list(self, newcell):
        if None is newcell.get_car:
            return []
        elif atom(newcell.get_car):
            return newcell.get_car
        else:
            self.get_list(newcell.get_cdr)
    
    def set_list(self, newcell):
        pass


def cons(a, b):
    newcell = Cell()
    newcell.set_car = a
    newcell.set_cdr = b
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
        root.set_car(1)
        root.set_cdr(2)
        print root.get_car()
        print root.get_cdr()
    except:
        pass
    else:
        pass
    finally:
        pass 

