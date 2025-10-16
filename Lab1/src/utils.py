def add(*args):
    return sum(args)

def substract(*args):
    fist = args[0]
    for arg in args[1:]:
        fist -= arg 
    return fist

