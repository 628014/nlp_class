
import nltk
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize

f = open("E:/课程学习/大三/大三上/自然语言处理/code/实验二/all.txt", 'r')
ll = f.read()
# 将符号都取代为空格，方便后面的split（）
ll = ll.replace(" ", ' ').replace(",,", ' ').replace("\n", ' ')
# 分词
word_list = word_tokenize(ll)
# 去重，用不到了就
# word_unique = np.unique(word_list)
# 确定次的频率
frequency = nltk.pos_tag(word_list)
plt = nltk.FreqDist(frequency)
# 化成字典的形式
d = dict(plt)
# n，v，adj，adv代表名词、动词、形容词、副词
n = {}
v = {}
adj = {}
adv = {}

# 将词进行分类存入，此处只选取了NN,VB,JJ,RB的形式，其余的词没有加入
for key in d.keys():
    if (key[1] == "NN"):
        n[key[0]] = d[key]
    elif (key[1] == "VB"):
        v[key[0]] = d[key]
    elif (key[1] == "JJ"):
        adj[key[0]] = d[key]
    elif (key[1] == "RB"):
        adv[key[0]] = d[key]

# 进行排序
n = list(sorted(n.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
v = list(sorted(v.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
adj = list(sorted(adj.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
adv = list(sorted(adv.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))

# 写到文件中
fo = open("E:/课程学习/大三/大三上/自然语言处理/code/实验二/result1.txt", 'w')
num = [50, 20, 20, 20]
word = ["名", "动", "形容", "副词"]
list2 = [n, v, adj, adv]
for j in range(4):
    fo.write("出现频率最高的前" + str(num[j]) + "个" + str(word[j]) + "词及次数：\n")
    for i in range(num[j]):
        fo.write((list2[j][i][0]) + " : " + str(list2[j][i][1]) + "\n")
f.close()
fo.close()


