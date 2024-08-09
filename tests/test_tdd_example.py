from lib.tdd_example import *

"""
given a number
it returns that number
"""
def test_given_num_non_3_5_divisible_returns_num():
    result = fizzbuzz(1)
    assert result == 1

"""
given a number divisible by 3
returns fizz
"""
def test_if_num_divisible_by_3_returns_fizz():
    result = fizzbuzz(9)
    assert result == "Fizz"

"""
given number divisible by 5
returns buzz
"""
def test_if_num_divisible_by_5_gives_buzz():
    result = fizzbuzz(5)
    assert result == "Buzz"

"""
given number divisible by both 3 and 5 
return fizzbuzz
"""
def test_if_num_divisible_by_both_3_and_5_return_fizzbuzz():
    result = fizzbuzz(45)
    assert result == "FizzBuzz"