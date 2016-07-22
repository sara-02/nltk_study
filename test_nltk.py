from nltk.corpus import brown
from nltk import sent_tokenize, word_tokenize, pos_tag
import os
import time
##for brown words corpus
def test_brown_corpus():
	brown_word=brown.words()[0:10]
	print "\n\nBrown word 1-10."
	print brown_word
	brown_word_tagged=brown.tagged_words()[0:10]
	print "\n\nBrown word tagged."
	print brown_word_tagged
	print "\n\nLength of brown words"
	print len(brown.words())

def test_book_resource():
	from nltk.book import *
	print "\n\nBooks imported successfully."
	print dir(text1)
	print len(text1)

def sentence_and_word_token():
	text='''Machine learning is the science of getting
	computers to act without being explicitly programmed
	 In the past decade, machine learning has given us self-
	 driving cars, practical speech recognition, effective web 
	 search, and a vastly improved understanding of the human 
	 genome. Machine learning is so pervasive today that you 
	 probably use it dozens of times a day without knowing it. 
	 Many researchers also think it is the best way to make 
	 progress towards human-level AI. 
	 In this class, you will learn about the 
	 most effective machine learning techniques, 
	 and gain practice implementing them and getting 
	 them to work for yourself. More importantly, 
	 you'll learn about not only the theoretical 
	 underpinnings of learning, but also gain the 
	 practical know-how needed to quickly and powerfully 
	 apply these techniques to new problems. Finally, 
	 you'll learn about some of Silicon Valley's best 
	 practices in innovation as it pertains to machine learning and AI.'''
	print "\n\nThe length of text is %d"%len(text)
	sents = sent_tokenize(text)
	print "\n\nAfter sentence tokenizing"
	print "\nThe length of text is %d"%len(sents)
	tokens = word_tokenize(text)
	print "Break the words into token."
	print "No. of tokens are %d"%len(tokens)
	tagged_tokens = pos_tag(tokens)
	print "Perform POS tagging."
	for i in tagged_tokens:
		print i

def test_funcs():
	funcs=[test_brown_corpus,test_book_resource,
	sentence_and_word_token]
	for f in funcs:	
		os.system('clear')
		print "Testing %s\n\n"%f
		f()
		time.sleep(3)

if __name__=="__main__":
	test_funcs()
			