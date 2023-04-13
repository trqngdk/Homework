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
