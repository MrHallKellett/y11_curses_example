from curses import wrapper
from random import randrange

WIDTH = 40
HEIGHT = 40

def main(screen):

    while True:
        char = None
        word = ""

        while char != 10:
            char = screen.getch()
            word += chr(char)

        x = randrange(0, WIDTH - len(word)-1)
        y = randrange(0, HEIGHT)

        screen.addstr(y, x, word)

wrapper(main)