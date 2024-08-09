from lib.example_one import *
import pytest

def test_with_two_hundred_words():
    text = " ".join(["word" for i in range(0, 200)])
    result = estimate_reading_time(text)
    assert result == 1.0

def test_with_four_hundred_words():
    text = " ".join(["word" for i in range(0, 400)])
    result = estimate_reading_time(text)
    assert result == 2.0

def test_with_three_hundred_words():
    text = " ".join(["word" for i in range(0, 300)])
    result = estimate_reading_time(text)
    assert result == 1.5

def test_with_empty_list():
    text = ""
    with pytest.raises(Exception, match="Can't estimate reading time for empty text."):
        estimate_reading_time(text)