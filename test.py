

def write_to_word_document(text, output_filename='output.docx'):

if __name__ == "__main__":
    # Replace the text with your desired content
    content_to_write = "Hello, this is a sample text that will be written to a Word document. Hello, this is a sample text that will be written to a Word document. Hello, this is a sample text that will be written to a Word document. Hello, this is a sample text that will be written to a Word document. Hello, this is a sample text that will be written to a Word document. "

    # Specify the output filename (optional, default is 'output.docx')
    output_filename = 'my_document.docx'

    # Call the function to write the text to the Word document
    write_to_word_document(content_to_write, output_filename)

    print(f'The text has been written to {output_filename}')
