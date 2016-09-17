'''
Created on Sep 8, 2016


'''

class Cell:

    def __init__(self):
        self.cell = [None, None]

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
        
    def get_list(self, newlist):
        if None is mylist.get_car:
            return []
        elif atom(newlist.get_car):
            return newlist.get_car
        else:
            self.get_list(newlist.get_cdr)
    
    def set_list(self, *args):
        if None is args.get_car:
            return []
        elif atom(args.get_car):
            return self.set_car(args)
        else:
            self.get_list(args.get_cdr)        

def cons(self, a, b):
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

if __name__ == '__main__':

        mylist = List()
        mylist.set_list([1, [2, [3, None]]])
        print mylist.cell
        print mylist.cell.pop()
        print mylist.cell.pop(0)
        print mylist.cell


