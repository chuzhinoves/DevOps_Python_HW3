def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        raise ZeroDivisionError("На 0 делить нельзя")
