def chromosome_check(sperm):
    """ Check X, Y chromosome to know if you have
    a son or a daughter.

    Args:
        sperm (str):

    Returns:
        str: Return birth result
    """
    if sperm is "XX":
        return "Congratulations! You're going to have a daughter."
    elif sperm is "XY":
        return "Congratulations! You're going to have a son."
    else:
        return "Congratulations! You're going to have a son."
