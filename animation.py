import time
import curses

def animated_text(stdscr):
    curses.curs_set(0)  
    dots = 0

    while True:
        stdscr.addstr(0, 1, 'Generating cloze' + '.' * dots)
        stdscr.refresh()
        time.sleep(0.5)
        
        dots += 1

        if dots == 4:
            stdscr.addstr(0,1, ' '*19)
            dots = 0

        
        
if __name__ == "__main__":
    curses.wrapper(animated_text)