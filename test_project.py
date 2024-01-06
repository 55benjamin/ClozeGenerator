from project import *
import pytest

# validate_limit takes 'input' as its sole parameter
# validate_limit should raise ValueError if input is not a positive int
def test_validate_limit():
    with pytest.raises(ValueError):
        validate_limit('not_an_int')
        validate_limit('-10')
        validate_limit('-3')
        validate_limit('0')

# validate_format takes 'source' and 'mode' as its two parameters
# validate_format should raise ValueError if the extension of the 'source' file does not match the chosen 'mode'/extension
def test_validate_format():
    with pytest.raises(ValueError):
        validate_format('file.txt','.pdf')
        validate_format('file.pdf','.txt')
        validate_format('file.docx','.pdf')


# get_content takes 'source' and 'mode' as its two parameters
# get_content calls one of 3 functions (read_txt, read_docx, read_pdf)
# get_content should raise a FileNotFoundError if the file dosen't exist 
def test_get_content():
    with pytest.raises(FileNotFoundError):
        get_content('imaginary.txt', '.txt')
        get_content('imaginary.pdf', '.pdf')
        get_content('imaginary.docx', '.docx')