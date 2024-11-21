import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

text = (
    "On a windy winter morning, a woman looked out of the window. "
    "The only thing she saw, a garden. A smile spread across her face as she spotted Maria, "
    "her daughter, in the middle of the garden enjoying the weather. It started drizzling. "
    "Maria started dancing joyfully. She tried to wave to her daughter, but her elbow was stuck, "
    "her arm hurt, her smile turned upside down. Reality came crashing down as the drizzle turned into a storm. "
    "Maria's murdered corpse consumed her mind. On a windy winter morning, a woman looked out of the window of her jail cell."
)

# Токенізація тексту
tokens = word_tokenize(text)

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))  # Завантаження англійських стоп-слів
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

def lemmatize_word(word):
    return lemmatizer.lemmatize(word, pos='v')  # 'v' означає дієслово

def stem_word(word):
    return stemmer.stem(word)

lemmatized_tokens = [lemmatize_word(word) for word in filtered_tokens]
stemmed_tokens = [stem_word(word) for word in filtered_tokens]

# Видалення пунктуації
punctuation = set(string.punctuation)
cleaned_tokens = [word for word in stemmed_tokens if word not in punctuation]


processed_text = " ".join(cleaned_tokens)

output_file = "output_text.txt"
with open(output_file, "w") as file:
    file.write(processed_text)

print(f"Оброблений текст збережено у файлі '{output_file}'.")