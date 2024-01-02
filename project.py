import re
import sys
import random
import spacy
import docx2txt
from os.path import splitext
from newspaper import Article
from pdfminer.high_level import extract_text



def main():


    filename = input("Please input filename with its extension (.txt):")

    content = get_content(filename)

    ext = splitext(filename)[1]

    if ext != '.txt':
        modified_sents = replace(content)
        
        with open('output.txt', 'w') as file:
            file.write('\n'.join(modified_sents))

    else:
        
        modified_paras = []

        for paragraph in content: 
            modified_sents = replace(paragraph)
            modified_paras.append(modified_sents)
            
        with open('output.txt', 'w') as file:
            for modified_para in modified_paras:
                file.write('\n'.join(modified_para))

        


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

def get_content(filename):

    accepted_exts = {
        '.txt': read_txt,
        '.docx': read_docx,
        '.pdf': read_pdf,
    }

    ext = splitext(filename)[1]
    

    if ext in accepted_exts:
        try:
            content = accepted_exts[ext](filename)
            return content

        except FileNotFoundError:
            # sys.exit if file does not exist
            raise ValueError("File does not exist")
            

    else:
        raise ValueError("Please ensure file is a .docx, .pdf or .txt file")


def replace(content):
    modified_sents = []

    nlp = spacy.load("en_core_web_sm")
            
    # call natural language processing object on str of text
    doc = nlp(content)

    
    for sent in doc.sents:
        # remove newlines from the end of sentence 
        text = sent.text.replace("\n", "")

        # randomise words in a sent for even distribution of blanks 
        randomized_sent = random.sample(list(sent), len(sent))

        
        
        for token in randomized_sent:
            
            if token.pos_ not in ['INTJ', 'NOUN', 'NUM', 'PUNCT', 'SYM', 'PROPN', 'X', 'SPACE']:

                # don't test students on contractions as they are too simplistic
                # \' uses an escape character to check if a literal apostrophe forms part of the token
                if '\'' not in str(token.text):
                    answer = token
                    
                    blank = '_' * (len(answer) + 5)
                    replacement = f'{blank}[{answer.pos_}][{answer.text}]'

                    # find the answer in text and replace it with replacement 
                    # do this only for the first occurrence to avoid repetition
        
                    modified_sent = re.sub(r'\b' + answer.text +  r'\b', replacement, text, count=1)
                    modified_sents.append(modified_sent)

                    break
                

    return modified_sents




if __name__ == "__main__":
     main()