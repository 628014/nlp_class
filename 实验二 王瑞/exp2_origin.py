import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# 训练集 语料库阅读器
train_text = state_union.raw("2005-GWBush.txt")
# 样本集 语料库阅读器
sample_text = state_union.raw("2006-GWBush.txt")

print(train_text[0:520])
print(sample_text[0:520])

# 训练分词器
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
# 训练好的分词器训练完成之后可以使用
tokenized = custom_sent_tokenizer.tokenize(sample_text)

# print(train_text)
# print(sample_text)
# print(custom_sent_tokenizer)
# print(tokenized[1:5])



def process_content():
    try:
        for i in tokenized[1:50]:
            # 分词
            words = nltk.word_tokenize(i)
            # 词性标注
            tagged = nltk.pos_tag(words)
            # 使用我的正则表达式对词性进行处理，就是设计一个模式
            # chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkGram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT|TO>+{"""
            # 正则表达式使用
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            # 输出
            print(chunked)
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(subtree)
            chunked.draw()
    except Exception as e:
        print(str(e))


# process_content()
