import sys

x = int #definisemo x kao tip promenjive INTEGER
x = input("Koji je Vaš omiljeni broj?") # definisemo varijablu/ promenjivu X tako da bude ono sto je input (odgovor/ulaz) za pitanje "What's your favorite number?"


if x == 100:
    print("Omiljeni broj je 100")
else:
    while x > str(100) or x < str(100):
        print("Tvoj omiljeni broj je " + x)

    sys.exit()
