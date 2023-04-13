# Homework

## Count the smiley faces!

**Description:** Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

**Example**: The binary representation of `1234` is `10011010010`, so the function should return `5` in this case

### Solution

```python
def count_bits(number):
    number = bin(number).replace("0b", "")
    return number.count("1")

```
