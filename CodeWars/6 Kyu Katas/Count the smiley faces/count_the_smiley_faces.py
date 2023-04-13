def count_smileys(arr):
    """
    Return the amount of smiley faces in an list/array
    Args:
        arr (arr): An array of symbol (":), :D, :-),..)
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
