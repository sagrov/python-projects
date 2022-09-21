import argparse

# importing arguments
parser = argparse.ArgumentParser()
parser.add_argument("operation", type=str)
parser.add_argument("firstnumber", type=int)
parser.add_argument("secondnumber", type=int)
args = parser.parse_args()

# dictionary to check arithmetic operation;
# "add", "sub" etc - keys;  "+", "-" etc - values
operations = {
    "add": "+",
    "sub": "-",
    "multi": "*",
    "div": "/",
}


def nums_operation():
    try:
        # f' - converts into a line; eval - evaluates a passed string as an expression
        return eval(f'{args.firstnumber} {operations[args.operation]} {args.secondnumber}')
    except(ZeroDivisionError):
        print("Can't divide by zero")
    except(EOFError, IndexError, SyntaxError, TypeError, KeyError, NameError, KeyboardInterrupt):
        print("Invalid syntax")


print(nums_operation())
