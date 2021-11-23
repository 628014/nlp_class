import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

def read(file):
    with open(file, 'r+',encoding='utf-8') as f:
        return f.read()


train_file_name = 'E:/课程学习/大三/大三上/自然语言处理/code/实验二 王瑞/data/train.txt'
sample_file_name = 'E:/课程学习/大三/大三上/自然语言处理/code/实验二 王瑞/data/sample.txt'

train_text = read(train_file_name)
sample_text = read(sample_file_name)
print(train_text)
print(sample_text)
# 训练模型
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
# 训练完成之后可以使用
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # 使用我的正则表达式对词性进行处理，就是设计一个模式
            # chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkGram = r"""Chunk: {<.*>+}
                                    }<VB.?>*<NN.?>*<VB.?|IN|DT|TO><VB.?>*<NN.?>{"""
            # chunkGram = r"""Chunk: {<.*>+}
            #                         }<VB.?|IN|DT|TO>+{"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print(chunked)
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(subtree)
            chunked.draw()
    except Exception as e:
        print(str(e))


process_content()
