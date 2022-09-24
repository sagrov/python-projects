import argparse
import math
import operator

# importing arguments
parser = argparse.ArgumentParser()
parser.add_argument("operation", type=str)
parser.add_argument("user_numbers", nargs="*", type=int)
args = parser.parse_args()


def nums_operation(operand, *numbers):
    try:
        # checking in operator module
        check_oper = getattr(operator, operand)
        return check_oper(*numbers)
    except Exception:
        try:
            # checking in math module
            check_math = getattr(math, operand)
            return check_math(*numbers)
        except Exception:
            # if neither of them passed or used more than 2 numbers
            return "Wrong Syntax or you've used more than 2 numbers"


print(nums_operation(args.operation, *args.user_numbers))
