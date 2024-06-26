import nltk
#nltk.download("punkt")
from nltk.stem.porter import PorterStemmer
import numpy as np

stemmer = PorterStemmer()

def tokenize(sentence): 
    return nltk.word_tokenize(sentence)

def stem(words):
    return stemmer.stem(words.lower())

def bag_of_words(tokenized_sentence, all_words):
    """
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog =   [ 0 ,     1,     0,    1,     0,       0,      0
    """

    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    return bag