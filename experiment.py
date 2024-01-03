import re
import curses
from os.path import splitext

def choose_option(stdscr):

    # clear screen and hide the cursor
    stdscr.clear()
    curses.curs_set(0)

    # add title text 
    stdscr.addstr(0, 1, "ClozeGenerator. Updated Jan 2023")
    stdscr.refresh()

    # record all mouse movements and get the mouse position
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    # option text to be displayed
    pdf_opt = "PDF (.pdf)"
    word_opt = "Word (.docx)"
    text_opt = "Text (.txt)"
    

    # display options on the screen
    stdscr.addstr(3,1, "To start, please select an input method:")
    stdscr.addstr(5,1, pdf_opt)
    stdscr.addstr(5,20, word_opt)
    stdscr.addstr(5,40, text_opt)

    
    stdscr.getch()

    # wait for user to click something
    while True: 
        if stdscr.getch() == curses.KEY_MOUSE:
            _, x, y, _, _ = curses.getmouse()

            if 0 <= x <= 15 and 3 <= y <= 10: 
                mode = '.pdf'

            elif 17 <= x <= 35 and 3 <= y <= 10:
                mode = '.docx'

            elif 37 <= x <= 55 and 3 <= y <= 10:
                mode = '.txt'

        if mode:
            break

    source = get_source(stdscr,mode)

    return source
    
        

 
def get_source(stdscr,mode):
    # clear out the terminal 
    stdscr.clear()

    # enable input mode and show the cursor
    curses.echo()  
    curses.curs_set(1)
    

    prompt = f"File where input text is stored (eg. extract{mode}):"

    
    while True: 
        # display the prompt 
        stdscr.addstr(1, 1, prompt)  

        # get the user's input 
        source = str(stdscr.getstr())

        
        if check_format(source, mode) is False: 
            error_msg = 'Please ensure the file and its extension are entered correctly. Alternatively, press Ctrl-C to exit the program'

            curses.start_color()

            # set red text against black background 
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

            # set the color pair to the error message text 
            stdscr.addstr(0,1, error_msg, curses.color_pair(1))
            
            # clear out the user's input, on the same row, and beginning column of input 
            stdscr.addstr(1, (1+len(prompt)), " " * (len(source)))

            stdscr.refresh()

            continue 

        elif check_format(source, mode) is True: 
            break 

    # disable input mode and hide the cursor          
    curses.noecho()  
    curses.curs_set(0)

    # clear out the terminal 
    stdscr.clear()

    return source 


def check_format(source, mode):
    
        pattern = f'.*\{mode}'

        match = re.search(pattern, source, re.VERBOSE)

        if match:
            return True

        elif not match:
            return False


        
curses.wrapper(choose_option)
