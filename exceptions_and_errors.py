"""
 Exceptions and Errors program
"""
"""
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Not supported type str. You should input a number")

try:
    x = 5
    y = 0

    z = x/y
except ZeroDivisionError:
    print("Must not divided by zero")

finally:
    print("All Done")
"""
def ask():
    """
    checking input that number is correct
    """
    while True:
        try:
            number=int(input("Please input a number : "))
        except ValueError:
            print("Not supported type str. You should input a number")
            continue
        except KeyboardInterrupt:
            print("You input wrong character")
            continue
        else:
            print("Correct inputs")
            return number**2
            break

        
