
# CS50P Capstone|Cloze Generator

## Demo
View the demo [here]()!

## The problem
A [comprehension cloze](http://tinyurl.com/CompreClozeExample) is an exercise whereby students, typically of the primary-school age (7 to 12 years old), are tasked with filling in blanks in an extract. 

The comprehension cloze aims to test students on:
* their knowledge of common [collocatons](https://en.wikipedia.org/wiki/Collocation) such as phrasal verbs and idioms
* their ability to sift out contextual clues and to make educated inferences

Creating a comprehension cloze is often tedious and mechanical. The steps below describe the typical process for creating one:
1. Find an appropriate extract
2. Copy the extract into a word document
3. Read each sentence
4. Categorise and pick out words to assess students on (such as prepositions or phrasal verbs)
5. Replace the words with blanks
6. Number the blanks
7. Total the total number of blanks/marks
8. Vet the passage to ensure there are an even distribution of blanks
9. Export the comprehension cloze
10. Create an answer sheet (answers and explanations)


## The solution
Cloze Generator aims to condense and automate the steps above, such that cloze passages can be created quickly and consistently with minimal user input. 


## Features 
* Supports text input and output for PDF/Word/.txt files
* Identifies and omits collocations and word types using [spaCy](https://spacy.io/usage/spacy-101) Natural Language Processing (NLP)
* Allows user to limit number of sentences/blanks/marks
* Creates separate question and answer sheet, where answer sheet lists original word and word type based on [16 common Universal Parts-of-Speech](https://universaldependencies.org/u/pos/)


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