def add(*args):
    return sum(args)

def substract(*args):
    fist = args[0]
    for arg in args[1:]:
        fist -= arg 
    return fist

def multiply(*args):
    first = args[0]
    for arg in args[1:]:
        first *= arg
    return first

def divide(*args):
    first = args[0]
    if first == 0:
        raise ValueError("Cannot divide by zero")
    for arg in args[1:]:
        if arg == 0:
            raise ValueError("Cannot divide by zero")
        first /= arg
    return first
