import nltk
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt
from collections import Counter

try:
    File = open('Milton-Paradise.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)

text = File.read()

def most_used_words(text):
    cnt = Counter(text)
    cort = cnt.most_common(10)

    x = [cort[el][0] for el in range(len(cort))]
    y = [cort[el][1] for el in range(len(cort))]

    plt.bar(x, y)
    plt.title("10 найбільш вживаних слів у тексті")
    plt.xlabel("Слова")
    plt.ylabel("Зустрічаються разів у тексті")
    plt.show()

# Стартовий текст
start_text = text.split()
most_used_words(start_text)

# Змінений текст
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

text2 = text.split()
finale_text = [word.strip(string.punctuation) for word in text2 if word.strip(string.punctuation).lower() not in stop_words]
most_used_words(finale_text)