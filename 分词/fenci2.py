# 目的 ：直接测试NLTK的基本功能和数据

# 例子 ： 下面主要测试了4种基本功能，分别为 ：
# 1. 测试英文 word tokenize 功能
# 2. 测试英文词性标注功能
# 3. 测试英文断句功能
# 4. 测试英文命名实体标注功能
# 每一个列子后面的结果都跟在后面了


# 1. 测试英文 word tokenize 功能
import nltk
text = "The Natural Language Toolkit, or more commonly NLTK, it's a suite of libraries and programs for  ...: symbolic and statistical natural language processing (NLP) for English written in the Python programming...:  language. It was developed by Steven Bird and Edward Loper in the Department of Computer and Informatio ...: n Science at the University of Pennsylvania. NLTK includes graphical demonstrations and sample data. It ...: is accompanied by a book that explains the underlying concepts behind the language processing tasks supp ...: orted by the toolkit, plus a cookbook."
tokens = nltk.word_tokenize(text)
print(tokens)

# 2.测试英文词性标注功能
tagged_tokens = nltk.pos_tag(tokens)
print(tagged_tokens[0:20])

# 结果 ： [('The', 'DT'),
#  ('Natural', 'NNP'),
#  ('Language', 'NNP'),
#  ('Toolkit', 'NNP'),
#  (',', ','),
#  ('or', 'CC'),
#  ('more', 'JJR'),
#  ('commonly', 'RB'),
#  ('NLTK', 'NNP'),
#  (',', ','),
#  ('it', 'PRP'),
#  ("'s", 'VBZ'),
#  ('a', 'DT'),
#  ('suite', 'NN'),
#  ('of', 'IN'),
#  ('libraries', 'NNS'),
#  ('and', 'CC'),
#  ('programs', 'NNS'),
#  ('for', 'IN'),
#  ('symbolic', 'JJ')]

# 3. 测试英文断句功能
sents = nltk.sent_tokenize(text)
print(sents)
# 结果 ：["The Natural Language Toolkit, or more commonly NLTK, it's a suite of libraries and programs for  ...: symbolic and statistical natural language processing (NLP) for English written in the Python programming...:  language.", 'It was developed by Steven Bird and Edward Loper in the Department of Computer and Informatio ...: n Science at the University of Pennsylvania.', 'NLTK includes graphical demonstrations and sample data.', 'It ...: is accompanied by a book that explains the underlying concepts behind the language processing tasks supp ...: orted by the toolkit, plus a cookbook.']

# 4. 测试英文命名实体标注功能

entities = nltk.chunk.ne_chunk(tagged_tokens)
print(entities)
# nltk.Tree.draw(entities)
# 结果 ：这是一个树形结构
# (S
#   The/DT
#   (ORGANIZATION Natural/NNP Language/NNP Toolkit/NNP)
#   ,/,
#   or/CC
#   more/JJR
#   commonly/RB
#   (ORGANIZATION NLTK/NNP)
#   ,/,
#   it/PRP
#   's/VBZ
#   a/DT
#   suite/NN
#   of/IN
#   libraries/NNS
#   and/CC
#   programs/NNS
#   for/IN
#   .../:
#   :/:
#   symbolic/JJ
#   and/CC
#   statistical/JJ
#   natural/JJ
#   language/NN
#   processing/NN
#   (/(
#   (ORGANIZATION NLP/NNP)
#   )/)
#   for/IN
#   (GPE English/NNP)
#   written/VBN
#   in/IN
#   the/DT
#   (GPE Python/NNP)
#   programming/NN
#   .../:
#   :/:
#   language/NN
#   ./.
#   It/PRP
#   was/VBD
#   developed/VBN
#   by/IN
#   (PERSON Steven/NNP Bird/NNP)
#   and/CC
#   (PERSON Edward/NNP Loper/NNP)
#   in/IN
#   the/DT
#   (ORGANIZATION Department/NNP)
#   of/IN
#   (ORGANIZATION Computer/NNP)
#   and/CC
#   (ORGANIZATION Informatio/NNP)
#   .../:
#   :/:
#   n/JJ
#   Science/NN
#   at/IN
#   the/DT
#   (ORGANIZATION University/NNP)
#   of/IN
#   (GPE Pennsylvania/NNP)
#   ./.
#   (ORGANIZATION NLTK/NNP)
#   includes/VBZ
#   graphical/JJ
#   demonstrations/NNS
#   and/CC
#   sample/JJ
#   data/NNS
#   ./.
#   It/PRP
#   .../:
#   :/:
#   is/VBZ
#   accompanied/VBN
#   by/IN
#   a/DT
#   book/NN
#   that/WDT
#   explains/VBZ
#   the/DT
#   underlying/JJ
#   concepts/NNS
#   behind/IN
#   the/DT
#   language/NN
#   processing/NN
#   tasks/NNS
#   supp/VBP
#   .../:
#   :/:
#   orted/VBN
#   by/IN
#   the/DT
#   toolkit/NN
#   ,/,
#   plus/CC
#   a/DT
#   cookbook/NN
#   ./.)



