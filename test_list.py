'''
Created on Sep 8, 2016

@author: oobasatoshi
'''
from list import *
import unittest


class Test(unittest.TestCase):


    def test_list(self):
        root = Cell()
        self.assertEquals(cons(1, 2),{1, 2})


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_list']
    unittest.main()