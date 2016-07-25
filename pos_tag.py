# You should use word_tokenize before pos tagging.
# Maxent treebank pos tagging model in NLTK by default.
import nltk

def pos_tagging():
	text = nltk.word_tokenize("Dive into NLTK: Part-of-speech tagging and POS Tagger")
	print text
	text_tagged = nltk.pos_tag(text)
	for i in text_tagged:
		print i
		print nltk.help.upenn_tagset(i[1])
		print "\n\n"

# def batch_pos_tagging():
# 	a=nltk.batch_pos_tag([[‘this’, ‘is’, ‘batch’, ‘tag’, ‘test’], 
# 		[‘nltk’, ‘is’, ‘text’, ‘analysis’, ‘tool’]])
# 	print a

in __name__=="__main__":
	pos_tagging()
	#batch_pos_tagging()