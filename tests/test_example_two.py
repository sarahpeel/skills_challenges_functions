from lib.example_two import improve_grammar
import pytest

def test_capital_and_no_punctuation_is_false():
    result = improve_grammar("Hello world")
    assert result == False

def test_no_capital_but_punctuation_is_false():
    result = improve_grammar("hello world!")
    assert result == False

def test_capital_and_punctuation_is_true():
    result = improve_grammar("Hello world!")
    assert result == True

def test_no_capital_and_no_punctuation_is_false():
    result = improve_grammar("hello world")
    assert result == False

def test_capital_and__comma_is_false():
    result = improve_grammar("Hello world,")
    assert result == False

def test_capital_and__colon_is_false():
    result = improve_grammar("Hello world:")
    assert result == False

def test_empty_string_gives_error():
    with pytest.raises(ValueError, match="No grammar in empty string."):
        improve_grammar("")