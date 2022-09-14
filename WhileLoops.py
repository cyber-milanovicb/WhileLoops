import sys

x = int
x = input("What's your favorite number?")


if x == 100:
    print("The favorite number is 100")
else:
    while x > str(100) or x < str(100):
        print("Your favorite number is " + x)

    sys.exit()
