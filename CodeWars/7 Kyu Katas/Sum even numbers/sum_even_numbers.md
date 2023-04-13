# Homework

## Count the smiley faces!

**Description:**
Complete the function that takes a sequence of numbers as single parameter. Your function must return the sum of **the even values** of this sequence.

Only numbers without decimals like `4` or `4.0` can be even.

The input is a sequence of numbers: integers and/or floats.

### Example

```
[4, 3, 1, 2, 5, 10, 6, 7, 9, 8]  -->  30   # because 4 + 2 + 10 + 6 + 8 = 30
[]                               -->  0
```

### Solution

```python
def sum_even_numbers(seq):
    """ Sum even numbers in a sequence

    Args:
        seq (arr): Sequence of given or random numbers.

    Returns:
        int: Return the total.
    """
    total = 0
    # Loop through all number in sequence.
    for number in seq:
        # Check for even numbers
        if not number % 2:
            total += number
    return total

```
