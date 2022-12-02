# %%
import re

import string
puncts = string.punctuation

from nltk.corpus import stopwords
engStopWords = stopwords.words('english')

from nltk import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

def preprocess_text(text_list, punctuation=puncts, stopwords=engStopWords, lemmatizer=lemmatizer, alpha=True):
    """
    Combines functions to preprocess tokens in documents
    Uses regex for cleaning documents

    Args:
        punctuation = string.punctuation
        stopwords = nltk.corpus import stopwords, stopwords.words('english')
        lemmatizer = WordNetLemmatizer() from nltk

    Returns: 
        list of cleaned text 
    """
    def del_stopWords(text, stopwords):
        """
        takes in texts splits into words and deletes if not in stopwords
        """
        word_list = text.split()
        text =" ".join([word for word in word_list if word not in stopwords])
        return text

    def del_punct(text, punctuation):
        """
        Takes in text splits into characters and deletes punctuations
        Punctiations imported usually from string.punctuation
        """
        text="".join([char for char in text if char not in punctuation])
        return text

    def lem_text(text, lemmatizer):
        """
        Takes in texts splits to words, and lemmatizes each word 
        Rejoins word with spaces
        Lemmatizer from nltk WorldNet()
        """
        word_list = text.split()
        text=" ".join([lemmatizer.lemmatize(word) for word in word_list])
        return text
    
    def alpha_only(text):
        """
        Remove non-alphabet words/characters
        """
        word_list = text.split()
        text=" ".join([word for word in word_list if word.isalpha()])
        return text

    text_clean=[]
    for text in text_list:
        text = text.lower() # lowers text
        text = re.sub(r'https?://\S+|www\.\S+', '', text) # remove urls
        text = re.sub(r'<.*?>', '', text) # remove htmls
        text = re.sub(r'\s+', ' ', text).strip() #removes trailing white spaces and changes multiple spaces to one
        text = re.sub(r'(?<=[/.,])(?=[^\s])', ' ', text) # adds a space after a period or comma, avoid joining two words
        text = del_punct(text, punctuation)
        text = del_stopWords(text, stopwords)
        text = lem_text(text, lemmatizer)
        if alpha==True:
            text=alpha_only(text)
        else: 
            pass
        text_clean.append(text)
    return text_clean