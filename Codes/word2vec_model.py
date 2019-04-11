#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 训练模型并保存
import nltk
nltk.download('stopwords')  #这一行只需要在代码初次执行时使用
from nltk import tokenize
from gensim.models import word2vec
from gensim.models.word2vec import LineSentence
import logging

from nltk.tokenize import sent_tokenize
sen = []
stop = set(nltk.corpus.stopwords.words('english'))

def model_train(textlines):    #textlines下的每一行为一段完整的文本
    for line in textlines:
        sentences = sent_tokenize(line)
        sentences = [l.strip('.') for l in sentences]
        for item in sentences:
            l = [i for i in item.lower().split()]
            sen.append(l)
    model = word2vec.Word2Vec(sentences = sentences)
    model.save('test.model')
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)   #日志记录

if __name__ == '__main__':
	import json
	with open('data.json','r') as f:
	    #加载文本库
        data = json.load(f)
        #由文本库训练词向量模型
	    model_train(data)
