import argparse

# importing arguments
parser = argparse.ArgumentParser()
parser.add_argument("firstnumber", type=str)
parser.add_argument("operation", type=str)
parser.add_argument("secondnumber", type=str)
args = parser.parse_args()


def nums_operation(first, operation, second):
    try:
        # f' - converts into a line; eval - evaluates a passed string as an expression
        print(eval(f'{first} {operation} {second}'))
    except (ZeroDivisionError):
        print("Can't divide by zero")


nums_operation(args.firstnumber, args.operation, args.secondnumber)

