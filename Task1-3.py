import argparse

parser = argparse.ArgumentParser()
parser.add_argument("user_input", type=str)
args = parser.parse_args()

def nums_operation(user_input):
    summ = 0
    for i in range (len(user_input)):
        if (args.user_input[0] == ' '):
            break
        elif (user_input[i] == '+' and args.user_input[i+1] == '+'):
            print ("False, None")
            break
        elif (args.user_input[i] == '-' and args.user_input[i+1] == '-'):
            print ("False, None")
            break
        elif (args.user_input[i] == '/' and args.user_input[i+1] == '/'):
            print("False, None")
            break
        elif (args.user_input[i] == '*' and args.user_input[i+1] == '*'):
            print("False, None")
            break

    for j in user_input:
        print("True", eval(user_input))


nums_operation(args.user_input)