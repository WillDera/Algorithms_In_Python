from struct import *

print("Float values are not supported")
user_input = input("Enter value: ")


def main(user_input):
    try:
        value = int(user_input)
        unicode_value = chr(value)
        print("unicode value of %s = %s" % (value, unicode_value))
    except ValueError:
        value = str(user_input)
        unicode_value = ord(value)
        print("unicode value of %s = %s" % (value, unicode_value))


if __name__ == "__main__":
    main(user_input)
