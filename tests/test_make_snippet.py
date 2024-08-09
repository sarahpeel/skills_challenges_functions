from lib.make_snippet import *

""" 
if string is empty
return empty string
"""
def test_if_string_is_empty_return_empty_string():
    result = make_snippet("")
    assert result == ""

"""
if string contains 3 words
return string
"""
def test_if_string_has_3_words_return_string():
    result = make_snippet("Hello, I'm Sarah")
    assert result == "Hello, I'm Sarah"

"""
if string contains 5 words
return string
"""
def test_if_string_has_5_words_return_string():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"

""" if string contains 6 words
return first 5 words and "..." """

def test_if_string_has_6_words_only_return_first_five_words():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five..."

"""
if words are separated with commas but not spaces
return string
"""
def test_if_6_words_separated_with_commas_not_spaces():
    result = make_snippet("one,two,three,four,five,six")
    assert result == "one,two,three,four,five,six"