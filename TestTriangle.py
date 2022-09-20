# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testValidInputA(self):
        self.assertEqual(classifyTriangle(2, 1, 0), 'InvalidInput1', 'Invalid input')

    def testValidInputB(self):
        self.assertEqual(classifyTriangle(1.5, 1, 1), 'InvalidInput2', 'Invalid input')

    def testValidInputC(self):
        self.assertEqual(classifyTriangle(201, 199, 199), 'InvalidInput0', 'Invalid input')

    def testValidTriangleA(self):
        self.assertEqual(classifyTriangle(199, 50, 1), 'NotATriangle', '199,50,1 is not a triangle')

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testIsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(10, 10, 12), 'Isosceles', '10, 10, 12 should be isosceles')

    def testIsoscelesTrianglesB(self):
        self.assertEqual(classifyTriangle(12, 10, 10), 'Isosceles', '12, 10, 10 should be isosceles')

    def testIsoscelesTrianglesC(self):
        self.assertEqual(classifyTriangle(10, 12, 10), 'Isosceles', '10, 12, 10 should be isosceles')

    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(10, 11, 12), 'Scalene', '10, 11, 12 should be Scalene')

    def testScaleneTrianglesB(self):
        self.assertEqual(classifyTriangle(10, 12, 11), 'Scalene', '10, 12, 11 should be Scalene')

    def testScaleneTrianglesC(self):
        self.assertEqual(classifyTriangle(12, 11, 10), 'Scalene', '12, 11, 10 should be Scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
