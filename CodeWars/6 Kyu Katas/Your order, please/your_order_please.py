def order(sentence):
    """ Using natural sort to sort words that consist
    numbers.

    Args:
        sentence (str): A sentence that contains
        numbers in words.

    Returns:
        str: Sort by the number of each word.
    """
    words = []
    for i in range(1, 10):
        for word in sentence.split():
            if str(i) in word:
                words.append(word)
    return " ".join(words)
