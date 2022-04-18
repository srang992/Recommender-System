import re
import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer


def clean_desc(s):
    s = str(s)
    s = s.lower()
    s = re.sub(r'[^a-zA-Z]', ' ', s)
    s = word_tokenize(s)
    p = [word for word in s if word not in set(stopwords.words('english'))]
    sent = ' '.join(p)
    return sent
