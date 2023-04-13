# Homework

## Convert a string to a number!

**Description:** We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

**Example**

```
"1234" --> 1234
"605"  --> 605
"1405" --> 1405
"-7" --> -7
```

### Solution

```python
def string_to_number(string):
    """Return a number from the given string.

    Args:
        string (str): String must be numbers.

    Returns:
        int: Return numbers.
    """
    return int(string)
```
