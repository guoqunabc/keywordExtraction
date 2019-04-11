#!/usr/bin/env python
# -*- coding: utf-8 -*-
#从摘要中提取候选词组

import nltk
nltk.download('wordnet')       #这一行只需要在代码初次执行时使用
from nltk.corpus import wordnet as wn
####################################
#此函数的功能对单词word进行整形，得到单词的词根
####################################
def get_lemma(word):  
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma  
    
def get_lemma2(word):
    lemma = nltk.stem.wordnet.WordNetLemmatizer()
    return lemma.lemmatize(word)


####################################
#此函数的功能是从文本text中提取出长度为2的名词词组，
#并对单词进行词根整形，放到数组keywords中
####################################
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




if __name__ == '__main__':
    import json
    #加载停用词列表
    with open('common_phrase.json', 'r', encoding = 'utf8') as fi:
        common_phrase = json.load(fi)

    #加载待处理的摘要文本
    with open('abstract.json','r') as f:
        data = json.load(f)
        #对文本进行分词提取
        phrases= extract(data)  
        candidate_words = []
        for word in phrases:
            li = word.lower().split()#将词组小写化并按空格分开成单词

            root_word = (' '.join([get_lemma(l) if len(l) > 4  else l for l in li]))  #获得单词的词根并重新合并成词组

            if root_word not in common_phrase:  #过滤掉常用词组
                  candidate_words.append(root_word)

    #将候选词组保存到json文件,以供后面的聚类使用
    with open('candidate_words.json','r') as fo:
        json.dump(candidate_words, fo)

