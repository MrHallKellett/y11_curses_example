import curses

def rgb(r, g, b):
    return "\x1b[38;2;{};{};{}m".format(r, g, b)

def load_colours():

    colour_map = [""] * 26

    with open("colours.txt") as f:
        lines = f.readlines()

    lines = sorted(lines)
    
    for line in lines:
        try:
            colour, _, code = line.strip().split("\t")
        except ValueError:
            continue
        initial = colour[0]
        index = ord(initial) - 65        
        colour_map[index] = eval(code)
    
    
    return colour_map


def game(screen):
    letter = "a"
    colours = load_colours()
    x, y = 0, 0
    colour = colours[0]
    index = 0

    screen.clear()
    while True:
        key = screen.getch()
        print(key)
        if 97 <= key <= 122:
            index = key - 97
            colour = colours[index]
            letter = chr(key)
            
        else:
            if key == 450:
                y -= 1
            elif key == 456:
                y += 1
            elif key == 452:
                x -= 1
            elif key == 450:
                x += 1
        
        screen.addstr(y, x, colour)

        


curses.wrapper(game)