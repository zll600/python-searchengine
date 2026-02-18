import re
import string

import Stemmer
from stop_words import get_stop_words

STOP_WORDS = get_stop_words('en')

PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))
STEMMER = Stemmer.Stemmer('english')

def tokenize(text: str) -> list[str]:
    return text.split()

def lowercase_filter(tokens: list[str]) -> list[str]:
    return [token.lower() for token in tokens]

def punctuation_filter(tokens : list[str]) -> list[str]:
    return [PUNCTUATION.sub('', token) for token in tokens]

def stopword_filter(tokens: list[str]) -> list[str]:
    return [token for token in tokens if token not in STOP_WORDS]

def stem_filter(tokens: list[str]) -> list[str]:
    return STEMMER.stemWords(tokens)

def analyze(text: str) -> list[str]:
    tokens = tokenize(text)
    tokens = lowercase_filter(tokens)
    tokens = punctuation_filter(tokens)
    tokens = stopword_filter(tokens)
    tokens = stem_filter(tokens)

    return [token for token in tokens if token]
