def count_bits(number):
    number = bin(number).replace("0b", "")
    return number.count("1")
