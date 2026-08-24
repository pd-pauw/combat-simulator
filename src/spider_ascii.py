import curses
#Drawn by Joan G. Stark (Spunk), https://www.asciiart.eu/art/4a6d088cff7d1bdf

MAX_WIDTH = 50
MAX_HEIGHT = 50

SPIDER = [
r"              (              ",
r"               )             ",
r"              (              ",
r"        /\  .-\"\"\"-.  /\   ",
r"       //\\/  ,,,  \//\\     ",
r"       |/\| ,;;;;;, |/\|     ",
r"       //\\\;-\"\"\"-;///\\  ",
r"      //  \/   .   \/  \\    ",
r"     (| ,-_| \ | / |_-, |)   ",
r"       //`__\.-.-./__`\\     ",
r"      // /.-(() ())-.\ \\    ",
r"     (\ |)   '---'   (| /)   ",
r"      ` (|           |) `    ",
r"        \)           (/      ",
]

def draw_warrior(window, start_y, start_x):
    for row, line in enumerate(SPIDER):
        draw_y = start_y + row
        if 0 <= draw_y < MAX_HEIGHT:
            try:
                window.addstr(draw_y, start_x, line)
            except curses.error:
                window.addstr( start_y, start_x, "Artwork to big")