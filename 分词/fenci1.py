# 目的 ： 介绍中文分词和英文分词主要介绍英文
#
# 中文 Jieba（重点），尝试三种分词模式与自定义词典功能、SnowNLP、THULAC、NLPIR、StanfordCoreNLP、
# 英文 NLTK、SpaCy、StanfordCoreNLP

# 例子1  ： NLTK 常用的几个 Tokenize
# 1、 SentencesSegment（分句）
# 2、 WordPunctTokenizer（分词）
# 3、 regexp_tokenize借助正则来实现分词

# 例子2 ： SpaCy 使用

# 例子3 ： StanfordCoreNLP使用


# 1、SentencesSegment（分句）
import nltk
from spacy.lang.en import English

sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
paragraph = "The first time I heard that song was in Hawaii on radio. ... I was just a kid, and loved it very much! What a fantastic song!"
sentences = sent_tokenizer.tokenize(paragraph)
print(sentences)

# 输出结果 ： ['The first time I heard that song was in Hawaii on radio.', '...', 'I was just a kid, and loved it very much!', 'What a fantastic song!']

# 2、WordPunctTokenizer（分词）

from nltk.tokenize import WordPunctTokenizer

sentence = "Are you old enough to remember Michael Jackson attending ... the Grammys with Brooke Shields and Webster sat on his lap during the show?"
words = WordPunctTokenizer().tokenize(sentence)
print(words)
# 输出结果 ：['Are', 'you', 'old', 'enough', 'to', 'remember', 'Michael', 'Jackson', 'attending', '...', 'the', 'Grammys', 'with', 'Brooke', 'Shields', 'and', 'Webster', 'sat', 'on', 'his', 'lap', 'during', 'the', 'show', '?']

# 3、 借助正则来实现分词
text = 'That U.S.A. poster-print costs $12.40...'
pattern = r'''''(?x)  # set flag to allow verbose regexps
...   ([A-Z]\.)+    # abbreviations, e.g. U.S.A.
...  | \w+(-\w+)*    # words with optional internal hyphens
...  | \$?\d+(\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
...  | \.\.\.      # ellipsis
...  | [][.,;"'?():-_`] # these are separate tokens; includes ], [
... '''
print(nltk.regexp_tokenize(text, pattern))

# 得到结果 ： [('', '', ''), ('', '', ''), ('', '-print', ''), ('', '', ''), ('', '', '')]
# 我想要的结果 ：['That', 'U.S.A.', 'poster-print', 'costs', '$12.40', '...']

# 明显不符合，会出现这样的问题是由于nltk.internals.compile_regexp_to_noncapturing()在V3.1版本的NLTK中已经被抛弃（尽管在更早的版本中它仍然可以运行），为此我们把之前定义的pattern稍作修改
pattern_true = r"""(?x)          # set flag to allow verbose regexps
       (?:[A-Z]\.)+      # abbreviations, e.g. U.S.A.
       |\d+(?:\.\d+)?%?    # numbers, incl. currency and percentages
       |\w+(?:[-']\w+)*    # words w/ optional internal hyphens/apostrophe
       |\.\.\.        # ellipsis
       |(?:[.,;"'?():-_`])  # special characters with meanings
      """
print(nltk.regexp_tokenize(text, pattern_true))

# 得到结果 ：['That', 'U.S.A.', 'poster-print', 'costs', '12.40', '...']


# 例子2 ： SpaCy 使用
import spacy
from spacy.tokens import Doc


class WhitespaceTokenizer(object):
    def __init__(self, vocab):
        self.vocab = vocab

    def __call__(self, text):
        words = text.split(' ')
        spaces = [True] * len(words)
        return Doc(self.vocab, words=words, spaces=spaces)


nlp = spacy.load('en_core_web_sm')
nlp.tokenizer = WhitespaceTokenizer(nlp.vocab)
doc = nlp(English)
print("spacy分词：")
print([t.text for t in doc])


# 例子3 ： StanfordCoreNLP使用
# from stanfordcorenlp import StanfordCoreNLP
#
# nlp = StanfordCoreNLP(r'E:\课程学习\大三\大三上\自然语言处理\课程资源\stanfordnlp\stanford-corenlp-4.3.0')
# sentence = "i 've had the player for about 2 years now and it still performs nicely with the exception of an occasional wwhhhrrr sound from the motor ."
# res = nlp.dependency_parse(sentence)
# print(res)
# 结果 ：
# [('ROOT', 0, 3), ('nsubj', 3, 1), ('aux', 3, 2), ('det', 5, 4), ('obj', 3, 5), ('case', 9, 6), ('advmod', 8, 7), ('nummod', 9, 8), ('nmod', 5, 9), ('advmod', 3, 10), ('cc', 14, 11), ('nsubj', 14, 12), ('advmod', 14, 13), ('conj', 3, 14), ('advmod', 14, 15), ('case', 18, 16), ('det', 18, 17), ('obl', 14, 18), ('case', 23, 19), ('det', 23, 20), ('amod', 23, 21), ('compound', 23, 22), ('nmod', 18, 23), ('case', 26, 24), ('det', 26, 25), ('nmod', 23, 26), ('punct', 3, 27)]
# 其中的那些数字代表的是第几个单词，但是它是从1开始数的，(‘ROOT’, 0, 3) 中的0不代表sentence中的单词
