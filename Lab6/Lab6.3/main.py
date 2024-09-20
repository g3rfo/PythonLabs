import re
def letter_output():
    text = input('Enter a text: ')
    if len(text) > 0:
        text = re.sub(r'[^a-zA-Z]', '', text)
        text = text.lower()
        unique_chars = list(set(text))
        unique_chars.sort()
        print("Unique chars: ", unique_chars)
    else:
        print("Please enter a valid text")

letter_output()