#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from calculate import Calculation


class TestCalculation(unittest.TestCase):
    def test_add(self):
        a = 1
        b = 2
        result = Calculation.add(a, b)
        assert result == 3

    def test_minus(self):
        a = 6
        b = 2
        result = Calculation.minus(a, b)
        assert result == 4

    def test_multiply(self):
        a = 3
        b = 4
        result = Calculation.multiple(a, b)
        assert result == 12

    def test_divide(self):
        a = 30
        b = 5
        result = Calculation.divide(a, b)
        assert result == 6


if __name__ == '__main__':
    suites = unittest.TestSuite()
    tests = [TestCalculation("test_add"), TestCalculation("test_minus"), TestCalculation("test_multiply"), TestCalculation("test_divide")]
    suites.addTests(tests)
    with open("TestResult.txt", "w") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suites)
