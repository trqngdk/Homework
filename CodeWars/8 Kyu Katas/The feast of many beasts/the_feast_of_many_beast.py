def feast(beast, dish):
    """
    Return True or False if first and last letter
    of beast is the same as dish or not.
    Args:
        beast (str): Input a name of the beast
        dish (str): Input a name of the dish
    """

    return beast[0] is dish[0] and beast[-1] is dish[-1]\
        