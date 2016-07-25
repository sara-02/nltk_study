from nltk import NaiveBayesClassifier
from nltk import classify
from nltk import NaiveBayesClassifier
from nltk import MaxentClassifier
import random
import os
import time

def gender_features1(word):
    return {'last_letter': word[-1]}

def gender_features2(name):
    features = {}
    features["firstletter"] = name[0].lower()
    features["lastletter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
       features["count(%s)" % letter] = name.lower().count(letter)
       features["has(%s)" % letter] = (letter in name.lower())
    return features

def gender_features3(name):
    features = {}
    features["fl"] = name[0].lower()
    features["ll"] = name[-1].lower()
    features["fw"] = name[:2].lower()
    features["lw"] = name[-2:].lower()
    return features

def model_dev(func_name): 
	from nltk.corpus import names   
	names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
	random.shuffle(names)
	print "Length of dataset %d"%len(names)
	random.shuffle(names)
	random.shuffle(names)
	print "How the data set looks"
	print names[0:10]
	print "Testing the output of feature extraction"
	print "For name Gary -- %s"%func_name('Gary')
	featuresets = [(func_name(n), g) for (n, g) in names]
	print "length of featureset data %d"%len(featuresets)
	print featuresets[0:10]
	train_set, test_set = featuresets[500:], featuresets[:500]
	print "Length of train data %d"%len(train_set)
	print "length of test data %d"%len(test_set)
	time.sleep(10)
	os.system('clear')

	print "\n\nNaive Bayes Classification\n\n"
	nb_classifier = NaiveBayesClassifier.train(train_set)
	check_list=['Gary', 'Shivam', 'Grace', 'Sarah', 'Shaym', 'Richa', 'Abhisheyk']
	for name in check_list:
		print "Naive gender classification of ---%s --is-- %s---"%(name,nb_classifier.classify(func_name(name)))
	print "The accuracy of the naive classifier is"
	print classify.accuracy(nb_classifier, test_set)
	print "The most informative features are:"
	print nb_classifier.show_most_informative_features(5)

	time.sleep(10)
	os.system('clear')
	print "\n\nMaxent Classification\n\n"
	mod=MaxentClassifier.train(train_set)
	for name in check_list:
		print "Maxent gender classification of ---%s --is-- %s---"%(name,mod.classify(func_name(name)))
	print "The accuracy of maxent is"
	print classify.accuracy(mod, test_set)
	print "The most informative features are:"
	print mod.show_most_informative_features(5)

if __name__=="__main__":
	func_list=[gender_features1, gender_features2, gender_features3]
	for i in func_list:
		print "For a different gender feature function"
		model_dev(i)
		time.sleep(20)