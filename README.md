
# CS50P Capstone|Cloze Generator

## Demo
View the demo [here]()!

## The problem
A [comprehension cloze](http://tinyurl.com/CompreClozeExample) is an exercise whereby students, typically of the primary-school age (7 to 12 years old), are tasked with filling in blanks in an extract. 

The comprehension cloze aims to test students on:
* their knowledge of common [collocations](https://en.wikipedia.org/wiki/Collocation) such as phrasal verbs and idioms
* their ability to sift out contextual clues to make educated inferences


Creating a comprehension cloze is often tedious and mechanical. Typically, the steps involve: 
1. Finding an appropriate extract
2. Copying the extract into a word document
3. Reading each sentence
4. Categorising and picking out words to assess students on (such as prepositions or phrasal verbs)
5. Replacing the words with blanks
6. Numbering the blanks
7. Totaling the total number of blanks/marks
8. Vetting the passage to ensure there are an even distribution of blanks
9. Exporting the comprehension cloze
10. Creating an answer sheet (answers and explanations)


## The solution
Cloze Generator aims to condense and automate the steps above, such that cloze passages can be created quickly and consistently with minimal user input and error.  


## Features 
* Supports text input and output for PDF/Word/.txt files
* Identifies and omits collocations and word types using [spaCy](https://spacy.io/usage/spacy-101) Natural Language Processing (NLP)
* Limits number of sentences/blanks/marks if required 
* Creates separate question and answer sheets
* Lists original word and word type in answer sheet based on [16 common Universal Parts-of-Speech](https://universaldependencies.org/u/pos/)


## How to run the Cloze Generator

### 1. Installing dependencies 
- Run `pip install -r requirements.txt` to install all dependencies.

### 2. Running the program
- Run `python3 project.py` to start the program. 


This will start an interactive terminal which will take you through the steps to use the Cloze Generator. 


## CS50P Video Requirements 
- [ ] Project Title
- [ ] Name
- [ ] GitHub and edX usernames 
- [ ] City and country
- [ ] Date video was recorded
- [ ] Submit https://forms.cs50.io/5e2dd8e8-3c8b-4eb2-b77d-085836253f26


## CS50P README Requirements
- [ ] Include the project title 
- [ ] Include YouTube video (<3 mins)
- [ ] Outline of project 
- [ ] What files contain 
- [ ] Choices debated on 
- [ ] ~500 words