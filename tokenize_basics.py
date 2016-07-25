from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


def sent_break():
	t = "This's a sentence tokenize test. This is two. is this sentence three. sent 4 is cool! Now see."

	print t 
	sent_token_list = sent_tokenize(t)
	print "The number of sentences are %d" % len(sent_token_list)
	for i in sent_token_list:
		print i

def word_break():
	t = "Hello World!, I am Sarah."
	print word_tokenize(t)

#There are various word tokenizers available in ntlk
# TreebankWordTokenizer, PunktWordTokenizer, and WordPunctTokenizer

if __name__=='__main__':
	print "\n\n Example of sentence tokenizing"
	sent_break()
	print "\n\n Example of word tokenizing"
	word_break()
