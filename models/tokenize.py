import nltk.data

try:
    nltk.data.find('tokenizers/punkt_tab.zip')
except LookupError:
    nltk.download("punkt_tab")

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def text_chunk(file: str):
    fp = open(file)
    data = fp.read()
    result = tokenizer.tokenize(data)
    fp.close()
    return result