# -*- coding: utf-8 -*-
import nltk
from nltk.tag.stanford import StanfordPOSTagger
from nltk.tokenize import word_tokenize

#the path where you have downloaded and unziped the full parser.
sp_dir = '/home/sarah/postagger/'
english_model = sp_dir + 'models/english-bidirectional-distsim.tagger'
chinese_model = sp_dir + 'models/chinese-distsim.tagger'
jar_path = sp_dir + 'stanford-postagger.jar'

#testing the english POS tagger
print "For the English model"
st_eng = StanfordPOSTagger(model_filename = english_model, path_to_jar = jar_path)
eng_sent = 'This is Stanford postagger in nltk for Python users.'
print eng_sent
eng_tokens = word_tokenize(eng_sent)
eng_tagged = st_eng.tag(eng_tokens)
for i in eng_tagged:
	print i

#testing for the chinese POS tagger
print "\n\nFor the Chinese model"
st_chi = StanfordPOSTagger(model_filename = chinese_model, path_to_jar = jar_path,encoding = 'utf-8')
chi_sent = '这 是 在 Python 环境 中 使用 斯坦福 词性 标 器'
print chi_sent
chi_tokens = word_tokenize(chi_sent)
chi_tagged = st_chi.tag(chi_tokens)
for i in chi_tagged:
	print i
#print st_chi.tag('这 是 在 Python 环境 中 使用 斯坦福 词性 标 器'.split())