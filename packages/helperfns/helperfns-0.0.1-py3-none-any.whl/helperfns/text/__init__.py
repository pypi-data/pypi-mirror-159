import re
import nltk

try:
    english_words = list(set(nltk.corpus.words.words()))
except Exception:
    nltk.download('words')
finally:
    english_words = list(set(nltk.corpus.words.words()))

def de_contract(word:str)->str:
    """
    De-contract strings

    This function de-contract strings. They converts strings like "i'm" to 'i am'

    Parameters
    ----------
    word : str
        A string that you want to de-contract
        
    Returns
    -------
    word: str
        A de-contracted word.

    See Also
    --------
    clean_sentence: cleans the text, by removing punctuations, numbers, tags, urls, etc from a sentence
    
    Examples
    --------
    >>> de_contract("I'm")
    "I am"
    """
    # specific
    word = re.sub(r"won\'t", "will not", word)
    word = re.sub(r"can\'t", "can not", word)

    # general
    word = re.sub(r"n\'t", " not", word)
    word = re.sub(r"\'re", " are", word)
    word = re.sub(r"\'s", " is", word)
    word = re.sub(r"\'d", " would", word)
    word = re.sub(r"\'ll", " will", word)
    word = re.sub(r"\'t", " not", word)
    word = re.sub(r"\'ve", " have", word)
    word = re.sub(r"\'m", " am", word)
    return word

def clean_sentence(sent:str, lower:bool = True)->str:
    """
    Clean Sentence
    
    This function cleans the text, by removing punctuations, numbers, tags, urls, etc from a sentence

    Parameters
    ----------
    sent : str
        An uncleaned sentence with text, punctuations, numbers and non-english words.
    lower : bool
        If lower is passed a returned sentence will be converted to lowercase, default is true
        
    Returns
    -------
    sent: str
        A cleaned string with text, punctuations, numbers and non-english removed.

    See Also
    --------  
    de_contract : de-contract strings by converting strings like "i'm" to 'i am'
    
    Examples
    --------
    >>> clean_sentence("text 1 # https://url.com/bla1/blah1/")
    'text'
    """
    
    sent = sent.lower() if lower else sent # converting the text to lower case
    sent = re.sub(r'(@|#)([A-Za-z0-9]+)', ' ', sent) # removing tags and mentions (there's no right way of doing it with regular expression but this will try)
    sent = re.sub(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", " ", sent) # removing emails
    sent = re.sub(r'https?\S+', ' ', sent, flags=re.MULTILINE) # removing url's
    sent = re.sub(r'\d', ' ', sent) # removing none word characters
    sent = re.sub(r'[^\w\s\']', ' ', sent) # removing punctuations except for "'" in words like I'm
    sent = re.sub(r'\s+', ' ', sent).strip() # remove more than one space
    words = list()
    for word in sent.split(' '):
        words.append(de_contract(word)) # replace word's like "i'm -> i am"
    return " ".join(w for w in words if w.lower() in english_words or not w.isalpha()) # removing non-english words


