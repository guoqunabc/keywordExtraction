


#########
#从训练好的模型中获取词向量
#########
def get_vector(ci_zu, model_path):  #分词词组， 词向量模型路径
    from gensim.models import Word2Vec
    model = Word2Vec.load(model_path)  #加载模型
    keys = set(ci_zu)
    vectors = []  # 词向量存储数组
    words = []  #分词存储词组
    for item in keys:
        l = item.lower().split()    #将分词小写化并按照空格拆分
        if len(l) != 1:  #判断分词是单个单词还是多个单词组成的词组
            vector = 0
            count = 0
            for it in l:
                if it in model:
                    vector += model[it]
                    count += 1
            #词组的向量取组成单词向量的平均
            if count != 0:
                phrase_vec = vector
                vectors.append(phrase_vec)
                words.append(item)
        else:
            if len(l) == 1:
                if item in model:
                    vectors.append(model[item])
                    words.append(item)
    return vectors, words


#########
#k-means聚类  主要用到的庫为nltk
#另外一种庫是sklearn
#########
def kmeans(X, Y, NUM_CLUSTERS):  #待聚类点阵，聚类个数
    import nltk
    from nltk.cluster import KMeansClusterer
    # 设定聚类数目
    k_cluster = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance,
                                repeats=15, avoid_empty_clusters=True)
    y = k_cluster.cluster(X, assign_clusters=True)
    t = dict(zip(Y, y))
    k = NUM_CLUSTERS
    result = []
    for i in range(0,k):
        cluster = [v for v in t.keys() if t[v] == i]
        result.append(cluster)
    print('输出聚类结果:')
    for item in result:
        print(item)