import pandas as pd
import string
def punc_clean(text):
    pun=string.punctuation
    samp_tex=str()
    for i in text:
        if i not in pun:
            samp_tex += i 
    return samp_tex
def preprocessing(text):
    text=punc_clean(text)
    text=text.lower()
    return text
if __name__=="__main__":
    preprocessing()