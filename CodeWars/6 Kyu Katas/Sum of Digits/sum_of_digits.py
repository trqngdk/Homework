def digital_root(number):
    """ Sum up all digits in a number until it only has 1 digit.

    Args:
        number (int): Input a number

    Returns:
        int: Return digital root.
    """
    sum_of_number = sum(map(int, str(number)))
    if sum_of_number > 9:
        return digital_root(sum_of_number)
    return sum_of_number
