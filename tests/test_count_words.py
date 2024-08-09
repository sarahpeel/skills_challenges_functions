from lib.count_words import count_words
"""
take empty string
return word count as zero
"""

#def test_empty_string_return_word_count_zero():
    #result = count_words("")
    #assert result == 0 

"""
take string with one word 
return word count as 1
"""
def test_string_containing_one_word_to_return_1():
    result = count_words("one")
    assert result == 1

def test_string_containing_two_words_to_return_2():
    result = count_words("one two")
    assert result == 2

"""
take 3 words with capital letters
return word count as 3
"""

def test_string_containing_3_words_and_caps_to_return_3():
    result = count_words("One Two Three")
    assert result == 3

"""
test hyphenated word only counts as one word
"""
def test_hyphenated_word_only_counts_as_one_word():
    result = count_words("check-in")
    assert result == 1

"""
test words separated by commas
"""
def test_word_separated_by_commas():
    result = count_words("one, two, three")
    assert result == 3

"""
test words with special characters
"""
def test_words_with_spec_chars():
    result = count_words("Happy! Birthday!")
    assert result == 2