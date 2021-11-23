
# Sometimes we want to capture the text that a user inputs when she is interacting with our program

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

# state_union 语料库阅读器
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
# 训练器 punkttokenizer(分句器) PunktSentenceTokenizer是NLTK中默认句子标记器(即sent_tokenize())的抽象类.
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
# 训练完成之后可以使用
tokenized = custom_sent_tokenizer.tokenize(sample_text)

# 当让，我也可以使用 sent_tokenize() https://github.com/nltk/nltk/blob/develop/nltk/tokenize/__init__.py#L79

# sent_tokenize()使用来自nltk_data/tokenizers/punkt/english.pickle的预训练模型.您还可以指定其他语言，
# NLTK中经过预先训练的模型的可用语言列表为:

# alvas@ubi:~/nltk_data/tokenizers/punkt$ ls
# czech.pickle     finnish.pickle  norwegian.pickle   slovene.pickle
# danish.pickle    french.pickle   polish.pickle      spanish.pickle
# dutch.pickle     german.pickle   portuguese.pickle  swedish.pickle
# english.pickle   greek.pickle    PY3                turkish.pickle
# estonian.pickle  italian.pickle  README

# 指定其他语言
# for sent in sent_tokenize(german_text, language='german'):
