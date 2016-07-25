import os
from nltk.parse import stanford

sd_dir ='/home/sarah/fullparser/'
parser_path = sd_dir + 'stanford-parser.jar'
os.environ['STANFORD_PARSER'] = parser_path
model_path = sd_dir + 'stanford-parser-3.4.1-models.jar'
os.environ['STANFORD_MODELS'] = model_path
lex_parser=sd_dir+'lexparser/englishPCFG.ser.gz'
parser = stanford.StanfordParser(model_path = lex_parser)
text="This is the English parser test", "The parser is from Stanford parser"
print text
sentences = parser.raw_parse_sents(text)
#GUI of parse tree for each line
for line in sentences:
    for words in line:
        words.draw()