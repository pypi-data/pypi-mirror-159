# Extra Spaces Remover

This project is an exta spaces remover that you can use to clean your text from unwanted extra spaces.

## Installation

Run the following to install:

```bash
pip install extraspaceremover
```

## Usage

```python
from spaceremover import remove_extra_spaces

text_with_extra_spaces = 'This is   an example   of text with extra spaces   '
cleaned_without_extra_spaces = remove_extra_spaces(text_with_extra_spaces)

print(cleaned_without_extra_spaces)

# Generates 'This is an example of text with extra spaces'
```

# Devoloping Extra Spaces Remover

To install  extraspaceremover, along with the tools you need to develop and run tests, run the following in your virtualenv:

```bash
pip install -e .[dev]
```