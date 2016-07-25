from nltk.tag import tnt
from nltk.corpus import treebank
import pickle

print len(treebank.tagged_sents())
train_data = treebank.tagged_sents()[:3000]
test_data = treebank.tagged_sents()[:3000]
print "\n\nTrain data is like\n %s" % train_data[0]
print "\n\nTest data is like\n %s" % test_data[0]

tnt_pos_tagger = tnt.TnT()
tnt_pos_tagger.train(train_data)
print "\n\nThe evaluation score is %d" % tnt_pos_tagger.evaluate(test_data)

f=open('tnt_treebank_pos_tagger.pickle', 'w')
pickle.dump(tnt_pos_tagger, f)
f.close()

test_tag=tnt_tagger.tag(nltk.word_tokenize("this is a tnt treebank tnt tagger"))
print "\n\n"
print test_tag


