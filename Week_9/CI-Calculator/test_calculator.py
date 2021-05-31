#! Python 3

"""
Simeon Patton
Test for Calculator App using circle CI
Inclass Activity week 9
OSU CS362 Spring 2021

"""

import calculator
import pytest

class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3,2)
    
    def test_subtract(self):
        assert 3 == calculator.subtract(96,3)