import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    max_y,max_x  = stdscr.getmaxyx()
    y = max_y // 2
    x = max_x // 2

    stdscr.refresh()
    window = curses.newwin(15,15, y, x)
    stdscr.refresh()
    window.box()
    window.addstr(1,2,"Main Menu")
    window.refresh()
    stdscr.getch()


if __name__ == "__main__":
    wrapper(main)
