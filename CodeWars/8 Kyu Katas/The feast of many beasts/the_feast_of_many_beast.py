def feast(beast, dish):
    """ Check to see whether the first and last letters of the beast
    match the first and last letters of the dish to see if the beast
    can bring that dish or not.

    Args:
        beast (str): Input the beast name
        dish (_str): Input the dish name

    Returns:
        str: Return results
    """

    return beast[0] is dish[0] and beast[-1] is dish[-1]
