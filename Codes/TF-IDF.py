#!/usr/bin/env python
# coding: utf-8

# In[4]:


import nltk
#nltk.download('wordnet')       #这句只需要在第一次使用时执行
from nltk.corpus import wordnet as wn

#得到单词的相似词根
def get_lemma(word):  
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma  
    
def get_lemma2(word):
    lemma = nltk.stem.wordnet.WordNetLemmatizer()
    return lemma.lemmatize(word)

def extract(text):
    from textblob import TextBlob
    blob = TextBlob(text)
    keywords = []
    #筛选出名词
    for keyphrase in blob.noun_phrases:  
        words = keyphrase.lower().split()
        if len(words) == 2:
            keyword = (' '.join([get_lemma(word) if len(word) > 4  else word for word in words]))
            keywords.append(keyword)
    return keywords  


# In[5]:


with open('CCF_abstract.txt','r') as f:
    lines = f.readlines()
    all_phrases = []
    for line in lines:
        all_phrases.extend(list(set(extract(line))))


# In[10]:


with open('CCF_abstract2.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        all_phrases.extend(list(set(extract(line))))


# In[3]:


from collections import Counter
dic = dict(Counter(all_phrases).most_common(3000)) 
import json
a = open('common_phrase.json', 'w', encoding = 'utf8')
json.dump(list(dic.keys()), a)

