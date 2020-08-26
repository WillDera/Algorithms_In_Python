user_input = input("Enter value: ")


def main(user_input):
    try:
        value = int(user_input)
        print("Input is an integer. ", value)
    except ValueError:
        try:
            value = float(user_input)
            print("Input is a float. ", value)
        except ValueError:
            print("Input is a str. ")


main(user_input)
