#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        num = a / b
    except (TypeError, ZeroDivisionError):
        num = None
    finally:
        print("Inside result: {}".format(num))
    return (num)
