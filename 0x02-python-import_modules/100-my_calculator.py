#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    len_arg = len(argv)
    if (len_arg != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        num1 = int(argv[1])
        sign = argv[2]
        num2 = int(argv[3])

        if sign == '+':
            res = add(num1, num2)
        elif sign == '-':
            res = sub(num1, num2)
        elif sign == '*':
            res = mul(num1, num2)
        elif sign == '/':
            res = div(num1, num2)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{} {} {} = {}".format(num1, sign, num2, res))
