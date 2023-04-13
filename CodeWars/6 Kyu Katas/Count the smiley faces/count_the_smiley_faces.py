def count_smileys(arr):
    """ Count number of smiley faces

    Args:
        arr (arr): Arrays of symbol (":)", ":D", ":-D",..)

    Returns:
        int: Return the amount of smiley face
    """

    smileys = []
    for symbol_part in arr:
        if len(symbol_part) == 2 and symbol_part[0] in [":", ";"] and \
                symbol_part[-1] in [")", "D"]:
            smileys.append(symbol_part)

        elif len(symbol_part) > 2 and symbol_part[0] in [":", ";"] and \
                symbol_part[1] in ["-", "~"] and symbol_part[-1] in [")", "D"]:
            smileys.append(symbol_part)
    return len(smileys)
