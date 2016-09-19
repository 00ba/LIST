# coding: utf-8

from cell import *
from list import *
import unittest


class Test(unittest.TestCase):


    def test_list(self):

        mylist = List()
        mylist.set_list(1, 2, 3)
        mylist.get_list()
        self.assertEquals(mylist.get_list(), [3, [2, [1, None]]])






if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_list']
    unittest.main()
