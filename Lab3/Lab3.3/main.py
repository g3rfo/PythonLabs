import re
string = input("Enter a string: ")

string = re.sub(r'[^\w]', ' ', string)
string = string.lower()
string = string.split()

difWords = set(string)

print("Unique words: ", difWords)