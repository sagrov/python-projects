import argparse

parser = argparse.ArgumentParser()
parser.add_argument("firstnumber", type=int)
parser.add_argument("operation", type=str)
parser.add_argument("secondnumber", type=int)
args = parser.parse_args()


def nums_operation():
  try:
    print(eval(str(args.firstnumber) + args.operation + str(args.secondnumber)))
  except (ZeroDivisionError):
    print("Can't divide by zero")

nums_operation()