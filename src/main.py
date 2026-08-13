import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    max_y,max_x  = stdscr.getmaxyx()
    y = max_y // 2
    x = max_x // 2
    window_left = curses.newwin(max_y,30, 0, 0)
    stdscr.refresh()
    window_middle = curses.newwin(max_y,100, 0, 32)
    stdscr.refresh()
    window_left.box()
    window_middle.box()
    window_left.addstr(4,2,f"{max_y} , {max_x}")
    window_left.addstr(1,2,"this is the left window")
    window_middle.refresh()
    window_left.refresh()
    stdscr.getch()


if __name__ == "__main__":
    wrapper(main)
