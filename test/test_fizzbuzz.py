from src import fizzbuzz

def test_return_1_for_1():
    assert fizzbuzz.do(1) == "1"

def test_return_fizz_for_3():
    assert fizzbuzz.do(3) == "fizz"

def test_return_buzz_for_5():
    assert fizzbuzz.do(5) == "buzz"

def test_return_fizz_for_multiples_of_3():
    assert fizzbuzz.do(9) == "fizz"
    assert fizzbuzz.do(12) == "fizz"
    assert fizzbuzz.do(21) == "fizz"

def test_return_buzz_for_multiples_of_5():
    assert fizzbuzz.do(10) == "buzz"
    assert fizzbuzz.do(20) == "buzz"
    assert fizzbuzz.do(55) == "buzz"
    