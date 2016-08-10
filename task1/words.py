from nltk import word_tokenize
import operator

_WORDS = {}

def count_word(word):
	if word in _WORDS:
		_WORDS[word] += 1
	else:
		_WORDS[word] = 1

def get_max():
	elem = max(_WORDS.iteritems(), key=operator.itemgetter(1))
	return elem

def get_ten_encountered_values():
	arr = []
	for i in range(10):
		arr.append(get_max())
		_WORDS.pop(elem[0], None)
	return arr

def split_words(text):
	words = word_tokenize(text)
	map(count_word, words)

def print_result():
	print "*" * 30
	print "10 encountered words"

	for k, v in get_ten_encountered_values().iteritems():
		print k + " - " + str(v)

	print "*" * 30