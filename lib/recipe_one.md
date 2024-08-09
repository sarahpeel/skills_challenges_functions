## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def estimate_reading_time(text)
#parameters:
#text: a string representing readable text
#return:
#a float representing reading time
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
given a test of 200 words
it will return readine time of 1
"""
estimate_reading_time("...200...")
# --> 1.0

""""
given a text of 400 words
it will return a reading time of 2
"""
estimate_reading_time("...400....")
# --> 2.0

"""
given a text of 300 words
it will return a reading time of 1.5
"""
estimate_reading_time("...300...")
# --> 1.5

"""
given an empty list
it will return an error
"""
estimate_reading_time("")
#raises error "Can't estimate reading time for empty text"


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
