# Homework

## Count the smiley faces!

**Description:** Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

**Example**

`[7]` should return 7, because it occurs 1 time (which is odd).

`[0]` should return 0, because it occurs 1 time (which is odd).

`[1,1,2]` should return 2, because it occurs 1 time (which is odd).

`[0,1,0,1,0]` should return 0, because it occurs 3 times (which is odd).

`[1,2,2,3,3,3,4,3,3,3,2,2,1]` should return 4, because it appears 1 time (which is odd).

### Solution

```python
import collections

def find_it(seq):
    if len(seq) == 0:
        return None

    string = collections.Counter(seq)
    for number in string:
        if string[number] % 2 == 1:
            return number

```
