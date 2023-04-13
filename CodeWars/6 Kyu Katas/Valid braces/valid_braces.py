def valid_braces(string):
    if len(string) % 2 != 0:
        return False
    right_way = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in string:
        if char in right_way:
            stack.append(char)
        else:
            if not stack:
                return False
            open_bracket = stack.pop()
            if char != right_way[open_bracket]:
                return False
    return not stack
