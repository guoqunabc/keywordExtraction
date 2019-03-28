# keywordExtraction TODO List

### 无监督学习方法：

1. PositionRank [\[link\]](https://github.com/ymym3412/position-rank)

   PositionRank is a keyphrase extraction method described in the ACL 2017 paper PositionRank: An Unsupervised Approach to Keyphrase Extraction from Scholarly Documents. This method search keyphrase by graph-based algorithm, which is biased PageRank by co-occurence word's position information. You can use this method not only English scholarly documents, but also any other language's document if you create your tokenizer (StanfordCoreNLP toolkit) for other language.

2. TF-IDF [\[link\]](https://github.com/titipata/keyphrase_extraction)

### 深度学习方法：

1. Word2Vec [\[link\]](https://github.com/bguvenc/keyword_extraction)

   Our model takes Word2Vec representations of words in a vector space. While we construct the Word2Vec model, we decide a threshold of counts of words because words that appear only once or twice in a large corpus are probably not unusual for the model, and there is not enough data to make any meaningful training on those words. A reasonable value for minimum counts changes between 0-100, and it depends on the size of corpora. Another critical parameter for Word2Vec model is the dimension of the vectors. This value changes between 100 and 400. Dimensions larger than 400 require more training but leads to more accurate models. I used Google News corpora which provided by Google which consist of 3 million word vectors. I did not remove stop words or infrequent words because these algorithms use windows and to find vector representations. So I need the nearby words to find vector representations.

   The second step of this algorithm is to find PageRank value of each word. PageRank algorithm works with random walk. The original PageRank algorithm takes internet pages as a node. In our model PageRank algorithm takes Word2Vec representations of words. The cosine distance is used to calculate edge weights between nodes. TextRank algorithm uses a similar method. While TextRank chooses the bag of word representations of words and a different similarity measure in finding edge weights, in this algorithm I used the Word2Vec representations and the cosine similarity. After PageRank values of words are found, we can get words which have the highest PageRank values. Finally, these words can be seen as a keyword of a text.

   这篇工作的不足：论文中的关键词可能为词库中没有的单词 (few-shot or zero-shot problem)

2. DeepRNN [\[link\]](https://github.com/basaldella/deepkeyphraseextraction)

   一号机已经完成CPU环境配置，还没有下载数据。

   - SimpleRNN.py : Bidirectional LSTM recurrent neural network that scans the text and selects the keyphrases. 

   - MergeRNN.py: Bidirectional LSTM recurrent neural network that scans the text two times: the left branch of the network reads the text and produces an encoded version of the document. This representation is then merged with the word embedding of each word and the text is scanned again using another Bidirectional LSTM that selects the keyphrases. 

   - AnswerRNN.py: inspired from Question Answering models, this network receives a series of candidate keyphrases generated using part-of-speech tag patterns and compares them with the document. It used two Bidirectional LSTMs to generate the representations of both the document and the keyphrase and another network on top with classifies each candidate KP. 

   - AnswerRNN2.py: evolution of AnswerRNN, borrows from Feng et Al., 2015 and Tan et al, 2016 similarity-based models.

   > Theano==0.9.0
   > nltk==3.2.4
   > numpy==1.13.1
   > matplotlib==2.0.2
   > Keras==2.0.5
   > h5py==2.7.0
   > scikit-learn==0.19.0

3.  Deep Keyphrase Generation based on ACL17 CopyNet [\[link\]](https://github.com/killa1218/CopyRNN-Keyword-Extraction)

   解决了identify keyphrases that do not appear in the text, nor capture the real semantic meaning behind the text的问题，如果代码可跑的话将会非常有东西。


