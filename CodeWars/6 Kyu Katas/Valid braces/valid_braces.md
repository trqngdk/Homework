# Homework

## Count the smiley faces!

**Description:**
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return `true` if the string is valid, and `false` if it's invalid.

This Kata is similar to the [Valid Parentheses](https://www.codewars.com/kata/valid-parentheses) Kata, but introduces new characters: brackets `[]`, and curly braces `{}`. Thanks to `@arnedag` for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: `()[]{}`.

### What is considered Valid?

A string of braces is considered valid if all braces are matched with the correct brace.

### Solution

```python
def valid_braces(string):
    if len(string) % 2 != 0:
        return False
    right_way = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in string:
        if char in right_way:
            stack.append(char)
        else:
            if not stack:
                return False
            open_bracket = stack.pop()
            if char != right_way[open_bracket]:
                return False
    return not stack

```
