import argparse

# importing arguments
parser = argparse.ArgumentParser(description="Type in some integers and operation")
parser.add_argument("firstnumber", type=int)
parser.add_argument("operation", type=str)
parser.add_argument("secondnumber", type=int)
args = parser.parse_args()


def nums_operation(first, operation, second):
    try:
        # f' - converts into a line; eval - evaluates a passed string as an expression
        return eval(f'{first} {operation} {second}')
    except (ZeroDivisionError):
        print("Can't divide by zero")
    except(EOFError, IndexError, SyntaxError, TypeError, KeyError, NameError, KeyboardInterrupt):
        print("Invalid syntax")


print(nums_operation(args.firstnumber, args.operation, args.secondnumber))
