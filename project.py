import re
import time
import random
import spacy
import curses
import docx2txt
from os.path import splitext
from pdfminer.high_level import extract_text



def main(stdscr):
    mode = get_mode(stdscr)

    while True: 
        try: 
            source = get_source(stdscr,mode)
            content = get_content(source, mode)
            break

        except ValueError:
            error_msg = 'File not found. Please try entering a different name and ensure the extension is correct.'

            show_error(stdscr,error_msg)

            stdscr.refresh()
            time.sleep(2)
            
            continue
    

    stdscr.clear()
    stdscr.addstr(0,1, "Generating cloze passage...")
    stdscr.refresh()
    

    if mode != '.txt':
        question_sents, answer_sents = replace(content)
        
        with open('answer.txt', 'w') as file:
            file.write('[ANSWER SHEET]\n')
            file.write('\n'.join(answer_sents))

        with open('question.txt', 'w') as file:
            file.write('[QUESTION SHEET]\n')
            file.write('\n'.join(question_sents))

    else:
        
        answer_paras = []
        question_paras = []

        for paragraph in content: 
            question_sents, answer_sents = replace(paragraph)
            answer_paras.append(answer_sents)
            question_paras.append(question_sents)
            
        with open('answer.txt', 'w') as file:

            file.write('[ANSWER SHEET]\n')

            for answer_para in answer_paras:
                file.write('\n'.join(answer_para))

        with open('question.txt', 'w') as file:
            file.write('[QUESTION SHEET]\n')

            for question_para in question_paras:
                file.write('\n'.join(question_para))

    stdscr.clear()
    success_msg = "Cloze passage generated! Press enter to exit."
    show_success(stdscr, success_msg)
    
    # wait for user to press enter to exit the program
    stdscr.getch()


def get_mode(stdscr):

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

    return mode 
     
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

        # get the user's input and decode it from a byte string to regular string
        source = stdscr.getstr().decode('utf-8')

        
        if check_format(source, mode) is False:
            error_msg = 'Please ensure the file and its extension are entered correctly. Alternatively, press Ctrl-C to exit the program'

            show_error(stdscr, error_msg)
            
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
    
    ext = splitext(source)[1]

    if str(ext) == str(mode):
        return True

    else:
        return False
        
def read_txt(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
        return content
    
def read_docx(filename):
    content = docx2txt.process(filename)
    return content 

def read_pdf(filename):
    content = extract_text(filename)
    return content 

def get_content(source, mode):

    accepted_modes = {
        '.txt': read_txt,
        '.docx': read_docx,
        '.pdf': read_pdf,
    }

    try:
        content = accepted_modes[mode](source)
        return content

    except FileNotFoundError:
        raise ValueError("File does not exist")
        
def replace(content):
    answer_sents = []
    question_sents = []

    nlp = spacy.load("en_core_web_sm")
            
    # call natural language processing object on str of text
    doc = nlp(content)

    index = 1 

    for sent in doc.sents:
        # remove newlines from the end of sentence 
        text = sent.text.replace("\n", "")

        # randomise words in a sent for even distribution of blanks 
        randomized_sent = random.sample(list(sent), len(sent))

        
        
        for token in randomized_sent:
            
            
            if token.pos_ not in ['INTJ', 'NOUN', 'NUM', 'PUNCT', 'SYM', 'PROPN', 'X', 'SPACE']:

                # don't test students on contractions as they are too simplistic
                # \' uses an escape character to check if a literal apostrophe forms part of the token
                if '\'' not in token.text:
                    answer = token
                    
                    blank = '_' * (len(answer) + 5)
                    replacement = f'{blank}[{answer.pos_}][{answer.text}]'

                    # find the answer in text and replace it with replacement 
                    # do this only for the first occurrence to avoid repetition
        
                    answer_sent = re.sub(r'\b' + answer.text +  r'\b', f' ({index}) {replacement}', text, count=1)
                    answer_sents.append(answer_sent)

                    question_sent = re.sub(r'\b' + answer.text +  r'\b', f' ({index}) {blank}', text, count=1)
                    question_sents.append(question_sent)
                    
                    index += 1

                    break
                

    return question_sents, answer_sents

def show_error(stdscr,error_msg):
    curses.start_color()

    # set red text against black background 
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

     # set the color pair to the error message text 
    stdscr.addstr(0,1, error_msg, curses.color_pair(1))

def show_success(stdscr, success_msg):
    curses.start_color()
     
    # set green text against black background 
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # set the color pair to the error message text 
    stdscr.addstr(0,1, success_msg, curses.color_pair(2))


if __name__ == "__main__":
    curses.wrapper(main)