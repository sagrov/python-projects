import argparse

parser = argparse.ArgumentParser()
parser.add_argument("user_input", type=str)
args = parser.parse_args()


def nums_operation(user_input):
    try:
        if line_clear(user_input):
            print("True,", eval(user_input))
        else:
            print("False, None")

    except (EOFError, IndexError, SyntaxError, TypeError, KeyError, NameError, KeyboardInterrupt):
        print("False, None123")


def line_clear(user_input):
    # checking if a first or last element is not a number; after that, checking if string has 2 math operators in a row and with .replace
    # we can replace '-' with '+'; and in last check, we remove every operator and check if remaining symbols are digits
    return user_input[0].isdigit() and user_input[-1].isdigit() and '++' not in user_input.replace('-', '+') and user_input.replace('-', '').replace('+', '').isdigit()


nums_operation(args.user_input)
