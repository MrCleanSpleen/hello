import time as t
import skilstak.colors as c

def print_murica(message):
    """Prints a message in red, white and blue. #Murica"""
    print(c.cl)
    while True:
        print(c.merica() + message, end =" ")

def print_plain(message):
    """Prints Hello World to the Console"""
    print(c.cl + message + c.x)

def print_multi(message):
    """Lights up text in random colors like a Christmas Tree"""
    while True:
        print(c.clear + c.multi(message))
        t.sleep(0.5)
def print_color(message):
    """Prints hello World in a random color"""
    print(c.cl + c.rc() + message + c.x)

def print_forever(message):
    """Prints Hello World in random colors all over the screen"""
    print(c.cl)
    while True:
        print(c.rc() + message + c.reset, end = " ")

def parse_args():
    """Allows the user to choose what the message should be and how it should be printed, ie 
    print_color, print_forever, print_multi, print_plain, or print_murica."""
    import sys
    name = "world"
    option = ""
    
    if len(sys.argv) > 2:
       option = sys.argv[1]
       who = sys.argv[2]
    elif len(sys.argv) == 2:
        if sys.argv[1].startswith("-"):
           option = sys.argv[1]
        else:
            who = sys.argv[1]
        return name, option
