# -*- coding: utf-8 -*-
import nltk
from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize

#the path where you have downloaded and unziped the ner parser.
sp_dir = '/home/sarah/nertagger/'
model1 = sp_dir + 'classifiers/english.all.3class.distsim.crf.ser.gz'
model2 = sp_dir + 'classifiers/english.conll.4class.distsim.crf.ser.gz'
model3 = sp_dir + 'classifiers/english.muc.7class.distsim.crf.ser.gz'
jar_path = sp_dir + 'stanford-ner.jar'

#our test sentence

eng_sent = 'Rami Eid has been studying at Stony Brook University in NY since 2007. He pays $30 daily'
print eng_sent
eng_tokens = word_tokenize(eng_sent)
#for 3 classes-Location, Person, Organization
print "\n\n 3 classes"
st_3 = StanfordNERTagger(model_filename = model1, path_to_jar = jar_path)
eng_tagged = st_3.tag(eng_tokens)
for i in eng_tagged:
	print i
#for 3 classes-Location, Person, Organization, Misc
print "\n\n 4 classes"
st_4 = StanfordNERTagger(model_filename = model2, path_to_jar = jar_path)
eng_tagged = st_4.tag(eng_tokens)
for i in eng_tagged:
	print i

#for 7 classes-Time, Location, Organization, Person, Money, Percent, Date 
print "\n\n 7 classes"
st_7 = StanfordNERTagger(model_filename = model3, path_to_jar = jar_path)
eng_tagged = st_7.tag(eng_tokens)
for i in eng_tagged:
	print i	