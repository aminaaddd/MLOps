def add(*args):
    # Return the sum of all arguments
    return sum(args)


def substract(*args):
    # substract all arguments from the first one
    first = args[0]
    for arg in args[1:]:
        first -= arg
    return first


def multiply(*args):
    first = args[0]
    for arg in args[1:]:
        first *= arg
    return first


def divide(*args):
    if len(args) == 0:
        raise IndexError("one argument required, but none given")

    first = args[0]
    if len(args) == 1:
        return first

    for arg in args[1:]:
        if arg == 0:
            raise ValueError("Cannot divide by zero")
        first /= arg

    if isinstance(first, float):
        return round(first, 4)
    return first
