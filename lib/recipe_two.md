## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def improve_grammar(text):
    """ verifies text starts with capital
    verifies text ends with punctuation

    Parameters: words -> a string containing a cpaital letter and punctuation

    Returns: Boolean -> true (grammar is correct)
                    -> false (grammar is incorrect)
    
    Side effects: none known

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a capital letter at the start
It returns False
"""
improve_grammar("Hello world") => False

"""
Given puncutation at the end
It returns False
"""
improve_grammar("hello world!") => False

"""
Given capital at start and punctuation at end
It returns True
"""
improve_grammar("Hello world!") => True

"""
Given no capital and no punctuation
It returns False
"""
improve_grammar("hello world") => False

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
