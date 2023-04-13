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
