import curses

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    stdscr.addstr(0, 1, "ClozeGenerator. Updated Jan 2023")

    stdscr.refresh()

    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    pdf_opt = "PDF (.pdf)"
    word_opt = "Word (.docx)"
    text_opt = "Text (.txt)"
    url_opt = "Enter a web URL"


    stdscr.addstr(3,1, "To start, please select an input method:")
    stdscr.addstr(5,1, pdf_opt)
    stdscr.addstr(5,20, word_opt)
    stdscr.addstr(5,40, text_opt)
    stdscr.addstr(5,60, url_opt)


    stdscr.getch()

    while True:
        if stdscr.getch() == curses.KEY_MOUSE:
            _, x, y, _, _ = curses.getmouse()

            if 0 <= x <= 15 and 3 <= y <= 10: 
                mode = 'pdf'

            elif 17 <= x <= 35 and 3 <= y <= 10:
                mode = 'docx'

            elif 37 <= x <= 55 and 3 <= y <= 10:
                mode = 'txt'

            elif 57 <= x <= 70 and 3 <= y <= 10:
                mode = 'url'

            

        
        stdscr.addstr(1,1,get_source(stdscr,mode))
        stdscr.refresh()
        

 
def get_source(stdscr,mode):
    stdscr.clear()
    curses.echo()  
    curses.curs_set(1)
    
    if mode != 'url':
        prompt = f"File where input text is stored (eg. extract.{mode}):"

    else:
        prompt = "Please input a link (eg. https://www.timeforkids.com/...):"
    
    stdscr.addstr(0, 1, prompt)  

    source = stdscr.getstr()
                            
    curses.noecho()  
    stdscr.clear()
    return source 

            

curses.wrapper(main)