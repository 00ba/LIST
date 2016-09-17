'''
Created on Sep 8, 2016

'''
from list import *
import unittest


class Test(unittest.TestCase):


    def test_list(self):
        root = Cell()
        root.set_car(1)
        root.set_cdr(2)
        self.assertEquals(root.get_car,1)
        self.assertEquals(root.get_cdr,2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_list']
    unittest.main()