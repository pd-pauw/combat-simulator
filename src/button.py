import curses

class Button:
    def __init__(self, text, y, x, parent_y, parent_x, callback):
        self.text = f"{text}"
        self.y = y
        self.x = x
        self.parent_y = parent_y
        self.parent_x = parent_x
        self.callback = callback

    def draw(self, window):
        window.addstr(
            self.y
        )
    
