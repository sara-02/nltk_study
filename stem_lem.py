from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

def porter_eg(word_list):
	porter_stemmer = PorterStemmer()
	for word in word_list:
		print "%s---%s"%(word, porter_stemmer.stem(word))

def lancaster_eg(word_list):
	lancaster_stemmer=LancasterStemmer()
	for word in word_list:
		print "%s---%s"%(word, lancaster_stemmer.stem(word))

def snowball_eg(word_list):
	snowball_stemmer = SnowballStemmer('english')
	for word in word_list:
		print "%s--%s"%(word, snowball_stemmer.stem(word))				

def lem_noun(word_list2):
	wordnet_lemmatizer = WordNetLemmatizer()
	for word in word_list2:
		print "%s--%s"%(word, wordnet_lemmatizer.lemmatize(word))

def lem_verb(word_list2):
	wordnet_lemmatizer = WordNetLemmatizer()
	for word in word_list2:
		print "%s--%s"%(word,wordnet_lemmatizer.lemmatize(word, pos = 'v'))

if __name__=="__main__":
	word_list = ['maximum', 'presumably', 'multiply',
	'provision', 'owed', 'ear', 'saying', 'crying', 'string',
	'meant', 'cement', 'joy']
	print "\n\n---Porter Stemmer---"
	porter_eg(word_list)
	print "\n\n---Lancaster Stemmer---"
	lancaster_eg(word_list)
	print "\n\n---Snowball Stemmer---"
	snowball_eg(word_list)
	word_list2=['dogs', 'churches', 'aardwolves',
	'abaci', 'hardrock', 'walking', 'are', 'is']
	print "\n\n---Noun Lemmatize---"
	lem_noun(word_list2)
	print "\n\n---Verb Lemmatize---"
	lem_verb(word_list2)