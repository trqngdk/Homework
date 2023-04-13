# Homework

## Count the smiley faces!

**Description:** `Digital root` is the recursive sum of all the digits in a number.

Given `n`, take the sum of the digits of `n`. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

**Example**

```
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
```

### Solution

```python
def digital_root(number):
    """
    Return digital root from a number.
    Args:
        number (int): A number that need to
            be sum until it has only 1 digit left.
    """

    sum_of_number = sum(map(int, str(number)))
    if sum_of_number > 9:
        return digital_root(sum_of_number)
    return sum_of_number

```
