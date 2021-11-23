import re

from nltk import word_tokenize


# 目的 ： 一套完整的流程，根据课本给出的一个例子，主要熟悉一些正则的例子

# 例子 ：
# 1. 去掉HTML标签(e.g. &amp;)
# 2. 去掉一些价值符号
# 3. 去掉超链接
# 4. 去掉一些专门名词缩写，简单来说就是字母比较少的词
# 5. 去掉多余的空格
# 6. 分词
text = '    RT @Amila #Test\nTom\'s newly listed Co  &amp; Mary\'s unlisted     Group to supply tech for nlTK.\nh $TSLA $AAPL https:// t.co/x34afsfQsh'

# 1. 去掉HTML标签(e.g. &amp;)
text_no_special_entities = re.sub(r'\&\w*;|#\w*|@\w*', '', text)
print('去掉特殊标签后的:', text_no_special_entities, '\n')
# 结果：
# 去掉特殊标签后的:     RT
# Tom's newly listed Co   Mary's unlisted     Group to supply tech for nlTK.
# h $TSLA $AAPL https:// t.co/x34afsfQsh


# 2. 去掉一些价值符号
text_no_tickers = re.sub(r'\$\w*', '', text_no_special_entities)
print('去掉价值符号后的:', text_no_tickers, '\n')
# 结果 ：
# 去掉价值符号后的:     RT
# Tom's newly listed Co   Mary's unlisted     Group to supply tech for nlTK.
# h   https:// t.co/x34afsfQsh


# 3. 去掉超链接
text_no_hyperlinks = re.sub(r'https?:\/\/.*\/\w*', '', text_no_tickers)
print('去掉超链接后的:', text_no_hyperlinks, '\n')
# 结果 ：
# 去掉超链接后的:     RT
# Tom's newly listed Co   Mary's unlisted     Group to supply tech for nlTK.
# h


# 4. 去掉一些专门名词缩写，简单来说就是字母比较少的词
text_no_small_words = re.sub(r'\b\w{1,2}\b', '', text_no_hyperlinks)
print('去掉专门名词缩写后:', text_no_small_words, '\n')
# 结果：
# 去掉专门名词缩写后:
# Tom' newly listed    Mary' unlisted     Group  supply tech for nlTK.

# 5. 去掉多余的空格
text_no_whitespace = re.sub(r'\s\s+', ' ', text_no_small_words)
text_no_whitespace = text_no_whitespace.lstrip(' ')
print('去掉空格后的:', text_no_whitespace, '\n')
# 结果 ：
# 去掉空格后的: Tom' newly listed Mary' unlisted Group supply tech for nlTK.

# 6. 分词
tokens = word_tokenize(text_no_whitespace)
print('分词结果:', tokens, '\n')
# 分词结果: ['Tom', "'", 'newly', 'listed', 'Mary', "'", 'unlisted', 'Group', 'supply', 'tech', 'for', 'nlTK', '.']
