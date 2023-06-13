import pytest

from series.series import fibonacci, lucas, sum_series

def test_fib_0():
    assert fibonacci(0) == 0

def test_fib_1():
    assert fibonacci(1) == 1

def test_fib_11():
    assert fibonacci(11) == 89

def test_lucas_0():
    assert lucas(0) == 2

def test_lucas_1():
    assert lucas(1) == 1

def test_lucas_11():
    assert lucas(11) == 199

def test_sum_fib():
    assert sum_series(7,0,1) == 13
  
def test_sum_lucas():
    assert sum_series(11,2,1) == 199