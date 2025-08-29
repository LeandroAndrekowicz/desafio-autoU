import nltk
nltk.data.path.append("/opt/render/project/src/.venv/nltk_data")

from nltk.corpus import stopwords
import nltk
import string

try:
    STOPWORDS = set(stopwords.words("portuguese"))
except LookupError:
    nltk.download("stopwords")
    STOPWORDS = set(stopwords.words("portuguese"))
    
class PreprocessText:
    @staticmethod
    def preprocess_text(text: str) -> str:
        """Remove stopwords e pontuação"""
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        tokens = [word for word in text.split() if word not in STOPWORDS]
        return " ".join(tokens)
