# coding: utf-8

'''
Created on Sep 8, 2016

'''
from cell import *
import unittest


class Test(unittest.TestCase):


    def test_cell(self):
        newcell = cons(1, 2)

        self.assertEquals(newcell.car(),1)
        self.assertEquals(newcell.cdr(),2)

        self.assertTrue(atom(1))
        self.assertTrue(atom('two'))
        self.assertFalse(atom([1, 2]))

        self.assertTrue(eq(1, 1))
        self.assertFalse(eq(1, 2))







if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_list']
    unittest.main()
