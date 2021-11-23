import nltk

from nltk.tag import *

# sentence = """Michale Scofield is an engineer. He is expert in java. He knows coding very well.
# He think world is like a big system of computers.A big system of computer involves the servers, servers are nothing but super-fast machines"""
#
# tagged_sent = pos_tag(sentence.split())
# print(tagged_sent)
#
# nouns = [word for word, pos in tagged_sent if pos == 'NNP' or pos == 'NN']
#
# print(nouns)
#
# freq_nouns = nltk.FreqDist(nouns)
#
# freq_nouns.most_common(3)

""" 1. 使用自带的pos_tag进行词性标注 """


def read(file):
    with open(file, 'r+') as f:
        return f.read()


file_name = 'E:/课程学习/大三/大三上/自然语言处理/code/实验二/all.txt'

read_txt = read(file_name)
# print(read_txt)
read_txt.replace(',', ' ').replace("\n", ' ').replace(",,", ' ')
# POS-tagger处理一个词序列，并且给每个词标定一个词性，以列表的形式返回
tagged_sent = pos_tag(read_txt.split())
# 统计次数并转化为列表的形式
d = dict(nltk.FreqDist(tagged_sent))

# print(tagged_sent)
# print(nltk.FreqDist(tagged_sent).most_common(3))
# 结果
# [(('the', 'DT'), 7213), (('a', 'DT'), 4061), (('of', 'IN'), 3976)]

# # n，v，adj，adv代表名词、动词、形容词、副词
# n = {}
# v = {}
# adj = {}
# adv = {}
#
# # 将词进行分类存入，此处只选取了NN(名词),VB(动词),JJ(形容词),RB(副词)，其余的词没有加入
# for key in d.keys():
#     if (key[1] == "NN"):
#         n[key[0]] = d[key]
#     elif (key[1] == "VB"):
#         v[key[0]] = d[key]
#     elif (key[1] == "JJ"):
#         adj[key[0]] = d[key]
#     elif (key[1] == "RB"):
#         adv[key[0]] = d[key]
#
# # 进行排序
# n = list(sorted(n.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
# v = list(sorted(v.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
# adj = list(sorted(adj.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
# adv = list(sorted(adv.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
#
# # 写到文件中
# fo = open("E:/课程学习/大三/大三上/自然语言处理/code/实验二/result3.txt", 'w')
# num = [50, 20, 20, 20]
# word = ["名", "动", "形容", "副词"]
# list2 = [n, v, adj, adv]
# for j in range(4):
#     fo.write("出现频率最高的前" + str(num[j]) + "个" + str(word[j]) + "词及次数：\n")
#     for i in range(num[j]):
#         fo.write((list2[j][i][0]) + " : " + str(list2[j][i][1]) + "\n")
# fo.close()


""" 2. 标注语料库"""

# 2.1 读取已经标注的语料库
# nltk语料库ue肚脐提供了统一接口，可以不必理会不同的文件格式。格式:语料库.tagged_word()/tagged_sents()。参数可以指定categories和fields
# print(nltk.corpus.brown.tagged_words())

# 2.2 Tagged Corpora
# from nltk.corpus import brown
# word_tag = nltk.FreqDist(brown.tagged_words(categories="news"))
#
# print([word+'/'+tag for (word,tag)in word_tag if tag.startswith('V')])
# ################下面是查找money的不同标注#################################
# wsj = brown.tagged_words(categories="news")
# cfd = nltk.ConditionalFreqDist(wsj)
# print(cfd['money'].keys())


# 2.3 简化标注语料库
from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories="news")
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
# 简化之后
print(len(tag_fd.keys()))
# 简化之前
print(len(nltk.corpus.brown.tagged_words()))

# 结果：
#
# 218
# 1161192


# 对于词性的标注
# 1. 默认的词性标注器  nltk自带英文标注器pos_tag

# 2. 标注语料库
# 2.1 读取已经标注的语料库
# 2.2 查询标注预料库里面的东西
# 2.3 探索已经标注的语料库

# 3. 自动标注

# 3.1 默认标注器
# 3.2 正则表达式标注器

# 4. N-gram标注
# 4.1 基础的一元标注器
# 4.2 一般的N-gram标注器
# 4.3 组合标注器
# 4.4 跨句子边界标注

# 5. 基于转换的标注：Brill标注器


