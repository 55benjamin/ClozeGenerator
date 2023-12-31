import sys
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

    print(content)
    for paragraph in content:
        
        doc = nlp(paragraph)

        for sent in doc.sents:
            text = sent.text.replace("\n", "")

            for token in sent:
                if token.pos_ in ['VERB', 'ADJ', "ADP", "DET", "ADV"]:
                #if token.pos_ not in ['INTJ', 'NOUN', 'NUM', 'PUNCT', 'SYM', 'PROPN']:
                    replacement = token
                    break

            modified_sent = text.replace(replacement.text,f'_____[{replacement.pos_}][{replacement.text}]' )
            modified_sents.append(modified_sent)


        with open('output.txt', 'w') as file:
            file.write('\n'.join(modified_sents))




if __name__ == "__main__":
     main()