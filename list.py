# coding: utf-8

class List(Cell):

    def __init__(self):
        self.root = Cell()

    def get_list(self):
        print self.root.cell

    def set_list(self, *args):
        for arg in args:
            if self.root.cell == []:
                self.root = cons(arg)
            else:
                self.root = cons(arg, self.root.cell)
        return self.root
