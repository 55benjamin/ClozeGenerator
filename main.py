import re
import sys
import random
import spacy



def main():
    filename = input("Please input filename with its extension (.txt):")

    content = get_content(filename)
    replace(content)


def get_content(filename):

    if filename.endswith('.txt'):
        try:
            with open(filename, 'r') as file:
                content = file.readlines()
                return content

        except FileNotFoundError:
            # sys.exit if file does not exist
            raise ValueError("File does not exist")

    else:
        raise ValueError("Please ensure file is a .txt file")


def replace(content):
    modified_sents = []

    nlp = spacy.load("en_core_web_sm")

    # each iteration of file.readlines is a paragraph
    for paragraph in content:
            
            # call natural language processing object on str of text
            doc = nlp(paragraph)

            
            for sent in doc.sents:
                # remove newlines from the end of sentence 
                text = sent.text.replace("\n", "")

                # randomise words in a sent for even distribution of blanks 
                randomized_sent = random.sample(list(sent), len(sent))
                

                for token in randomized_sent:
                    if token.pos_ in ['VERB', 'ADJ', "ADP", "DET", "ADV"]:
                    #if token.pos_ not in ['INTJ', 'NOUN', 'NUM', 'PUNCT', 'SYM', 'PROPN']:
                        answer = token
                        break
                        
                blank = '_' * (len(answer) + 5)
                replacement = f'{blank}[{answer.pos_}][{answer.text}]'


                # find the answer in text and replace it with replacement 
                # do this only for the first occurrence to avoid repetition
                modified_sent = re.sub(r'\b' + answer.text +  r'\b', replacement, text, count=1)
                        
    
                modified_sents.append(modified_sent)


            with open('output.txt', 'w') as file:
                file.write('\n'.join(modified_sents))




if __name__ == "__main__":
     main()