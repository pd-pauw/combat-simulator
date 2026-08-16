import curses

MAX_WIDTH = 50
MAX_HEIGHT = 50

#Drawn by Joan G. Stark (Spunk), https://www.asciiart.eu/art/f629685e70c95c57
WARRIOR = [
r" /\ ",
r" || ",
r" || ",
r" || ",
r" ||           {} ",
r" ||          .--. ",
r" ||         /.--.\ ",
r" ||         |====| ",
r" ||         |`::`| ",
r"_||_    .-;`\..../`;_.-^-._ ",
r" /\\   /  |...::..|`   :   `| ",
r" |:'\ |   /'''::''|   .:.   | ",
r"  \ /\;-,/\   ::  |..:::::..| ",
r"   \ <` >  >._::_.| ':::::' | ",
r"      `""`  /   ^^  |   ':'   | ",
r"          |       \    :    / ",
r"          |        \   :   /  ",
r"          |___/\___|`-.:.-` ",
r"           \_ || _/    ` ",
r"           <_ >< _> ",
r"           |  ||  | ",
r"           |  ||  | ",
r"          _\.:||:./_ ",
r"         /____/\____\ "
]

def draw_warrior(window, start_y, start_x):
    for row, line in enumerate(WARRIOR):
        draw_y = start_y + row
        if 0 <= draw_y < MAX_HEIGHT:
            try:
                window.addstr(draw_y, start_x, line)
            except curses.error:
                window.addstr( start_y, start_x, "Artwork to big")