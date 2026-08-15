import curses
from enum import Enum
from curses import wrapper
from warrior_ascii import draw_warrior

class Main_menu_option(Enum):
    START = 1 
    CLOSE = 2

def main(stdscr):
    curses.resize_term(50,150)
    stdscr.clear()
    stdscr.refresh()
    max_y,max_x  = stdscr.getmaxyx()
    curses.curs_set(0)
    draw_main_menu(stdscr, max_y, max_x)
    stdscr.getch()

def draw_main_menu(stdrc, max_y, max_x):
    #left part
    LEFT_WIDTH = 50
    start_line_left = (max_y//2)-12 if (max_y//2)-12 >= 0 else 0
    window_left = curses.newwin(max_y, LEFT_WIDTH, 0 , 0)
    draw_warrior(window_left, start_line_left, 0 )
    window_left.refresh()

    #middle window
    MIDDLE_WIDTH = 50
    window_middle = curses.newwin(max_y,MIDDLE_WIDTH, 0, LEFT_WIDTH)
    window_middle.addstr(1,1, "Main menu")
    window_middle.addstr(2,1, f"start y: {start_line_left}")
    window_middle.refresh()

    #right window
    RIGHT_WIDTH = 50
    start_line_rigth = (max_y//2)-12 if (max_y//2)-12 >= 0 else 0
    window_right = curses.newwin(max_y, RIGHT_WIDTH, 0 , LEFT_WIDTH + MIDDLE_WIDTH)
    draw_warrior(window_right, start_line_rigth, 0 )
    window_right.refresh()


if __name__ == "__main__":
    wrapper(main)
