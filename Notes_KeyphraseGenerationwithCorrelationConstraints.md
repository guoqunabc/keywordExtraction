传统方法：忽略相关性， 有重复和覆盖范围问题

新的seq2seq CorrRNN

* use a coverage vector 来指示词语是否被概括过
* 考虑之前的短语来减少重复

## 1 Introduction

关键短语：在文章中出现的和未出现的

传统方法：提取重要的text spans并排序，不能处理未出现的关键短语

处理absent keyphrases：生成方法 使用Seq2Seq framework with a

 copy mechanism以激励rare word generation

编码器将文本压缩成dense vector，解码器用RNN生成

一篇文章有多个关键短语，使用多个文档-关键词对来训练

忽略了目标关键短语之间的联系，不是一（文档）对多（关键词）的

只能依据原文本，忽略了已经生成的短语

因此会有**duplication issue**和**coverage issue**

解决方法：生成->检查->生成->全部覆盖

新的seq2seq架构：CorrRNN

相关约束：关键词全覆盖且不重复

使用了一种覆盖机制来记录文章的哪部分被概括了

提出了一种review机制来考虑已经生成的关键词

review机制：对已生成词和正在生成的词的相关性建模，从已有的seq2seq模型扩展，捕捉关键词生成中的一对多关系

在三个benchmark数据集上测试，比现有方法好很多

文章主要贡献：

* 提出一对多关系模型
* 提出CorrRNN
* 测试CorrRNN可靠性

## 2 相关工作

两类关键词方法：

* 基于抽取
* 基于生成

基于抽取：从文本里抽取两个单词长的短语

第一阶段：构建候选词组

第二阶段：排序

有监督/无监督

基于生成：NLG，可以生成未出现词

* encoder-decoder framework with a copy mechanism

这篇文章使用的是基于生成的方法

主要区别：考虑相关性

## 3 KeyphraseGenerationwithCorrelation

### 3.1 Problem Formalization

数据集$D={x_i,p_i}$

x是文本，p是关键词集合，

以前的工作是最大化$\prod_{i=1}^{N}\prod_{j=1}^{M_{i}}P(p_{i,j}|x_{i})$

本文最大化$\prod_{i=1}^{N}\prod_{j=1}^{M_{i}}P(p_{i,j}|x_{i}，p_{i,l<j})$

### 3.2 Seq2Seq Model with Copy Mechanism

编码器把变长文本变成向量

解码器从向量中生成文本

纯生成方法不能生成文本外的词，因此引入copy mechanism

### 3.3 Model Correlation

使用coverage mechanism解决覆盖度问题

提出review mechanism解决重复问题

![](https://github.com/keel-keywordextraction-entitylinking/keywordExtraction/blob/master/Material_For_Notes/corrRNN.png?raw=true)

#### 3.3.1 Coverage Mechanism

关键词对应位置

看哪些重要位置没被覆盖

#### 3.3.2 Review Mechanism

构造已生成短语的上下文信息

## 4 Experiment Settings

### 4.1 Implementation Details

切分，小写化，digit replacement

每篇文章有一个源文本和对应的多个短语（**有监督**）

target phrase最多十个

源码：给了个空地址

### 4.2 Datasets

KP20k训练

验证：

* NUS
* Semeval-2010
* Krapivin

### 4.3 Baseline Models

基于抽取的：Tf-idf，TextRank，SingleRank，ExpandRank，TopicRank，KEA，Maui

基于生成的：RNN，CopyRNN

前五个无监督，后四个有监督

### 4.4 Evaluation Metrics



## 5 Results and Analysis

![](https://github.com/keel-keywordextraction-entitylinking/keywordExtraction/blob/master/Material_For_Notes/CorrRNN_result.png?raw=true)

对未知domain表现更好

总结：potential