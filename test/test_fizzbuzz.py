from src import fizzbuzz

def test_return_1_for_1():
    assert fizzbuzz.do(1) == "1"

def test_return_fizz_for_3():
    assert fizzbuzz.do(3) == "fizz"