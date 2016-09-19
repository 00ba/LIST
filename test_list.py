'''
Created on Sep 8, 2016

'''
from list import *
import unittest


class Test(unittest.TestCase):


    def test_list(self):
        root = Cell()
        root = root.cons(1, [2, [3, None]])

        self.assertEquals(root.get_car(),1)
        self.assertEquals(root.get_cdr(),[2, [3, None]])

        self.assertTrue(atom(1))
        self.assertTrue(atom('two'))
        self.assertFalse(atom([1, 2]))

        self.assertTrue(eq(1, 1))
        self.assertFalse(eq(1, 2))

        mylist = List()
        mylist.set_list(1, 2, 3)
        self.assertEquals(mylist.get_list, [3, [2, [1, None]]])






if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_list']
    unittest.main()
