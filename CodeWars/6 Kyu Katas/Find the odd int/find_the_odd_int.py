import collections


def find_it(seq):
    if len(seq) == 0:
        return None

    string = collections.Counter(seq)
    for number in string:
        if string[number] % 2 == 1:
            return number
