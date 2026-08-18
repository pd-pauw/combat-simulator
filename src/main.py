import curses
from enum import Enum
from curses import wrapper
from warrior_ascii import draw_warrior

class Main_menu_option(Enum):
    START = 1 
    CLOSE = 2

def main(stdscr):
    curses.resize_term(50,150)

    # Enable mouse events
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    stdscr.clear()
    stdscr.refresh()
    max_y,max_x  = stdscr.getmaxyx()
    curses.curs_set(0)
    draw_main_menu(stdscr, max_y, max_x)


   

def draw_main_menu(stdrc, max_y, max_x):
    
    #left part
    LEFT_WIDTH = 30
    start_line_left = (max_y//2)-12 if (max_y//2)-12 >= 0 else 0
    window_left = curses.newwin(max_y, LEFT_WIDTH, 0 , 0)
    draw_warrior(window_left, 0, 0 )
    window_left.refresh()

    #middle window
    MIDDLE_WIDTH = 50
    start_button_y = 12
    start_button_x =  20
    start_button_text = "[  Start   ]"
    window_middle = curses.newwin(max_y,MIDDLE_WIDTH, 0, LEFT_WIDTH)
    window_middle.addstr(1,10, "Main menu")
    window_middle.addstr(start_button_y,start_button_x, start_button_text, curses.A_REVERSE)
    #window_middle.addstr(12,20, f"Start")
    window_middle.addstr(14,20, f"Exit")
    window_middle.box()
    window_middle.refresh()

    #right window
    RIGHT_WIDTH = 30
    start_line_rigth = (max_y//2)-12 if (max_y//2)-12 >= 0 else 0
    window_right = curses.newwin(max_y, RIGHT_WIDTH, 0 , LEFT_WIDTH + MIDDLE_WIDTH)
    draw_warrior(window_right, 0, 0 )
    window_right.refresh()
    while True:
        key = stdrc.getch()

        if key == ord("q"):
            break

        if key == curses.KEY_MOUSE:
            try:
                _, mx, my, _, button_state = curses.getmouse()
                if button_state & curses.BUTTON1_CLICKED:
                    if(start_button_x + LEFT_WIDTH <= mx < start_button_x + 
                       len(start_button_text) + LEFT_WIDTH 
                       and start_button_y == my ):
                        window_middle.addstr(5,20,"button clicked")
                        window_middle.refresh()
                        stdrc.getch()
            except curses.error:
                pass




if __name__ == "__main__":
    wrapper(main)
