try:
    number = int(input("Type a number: "))
    print(1/number)
except ZeroDivisionError:
    print("Man, can't divide that shit by zero")
except ValueError:
    print("Bro, is that a number?")
except Exception:
    print("Ok, man. Something went wrong. try again later")
finally:
    print("Well, done!")