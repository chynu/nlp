"""
First test file. Trying out nltk functions on the 
gutenberg corpora provided by nltk.
"""

import nltk
from nltk.corpus import gutenberg

def main():
	gut()

def gut():
	"""
	Execution function for the gutenberg library.
	"""

	emma = get_counts("austen-emma.txt")
	emma_info = {
		"char_per_word": emma["chars"]/emma["words"],
		"word_per_sent": emma["words"]/emma["sents"],
		"word_freq": emma["words"]/emma["vocab"]
	}

	print(" ======== Emma by Jane Austen ======== ")
	print("Number of characters: " + str(emma["chars"]))
	print("Number of words: " + str(emma["words"]))
	print("Number of sentences: " + str(emma["sents"]))
	print("")
	print("Characters per word: " + str(emma_info["char_per_word"]))
	print("Words per sentence: " + str(emma_info["word_per_sent"]))
	print("Word frequency: " + str(emma_info["word_freq"]))


def get_counts(fileid):
	"""
	Returns the character, word, sentence, and unique-word counts of a given
	text corpora.
	"""
	ret = {
			"chars": len(gutenberg.raw(fileid)), # characters,
			"words": len(gutenberg.words(fileid)), # words
			"sents": len(gutenberg.sents(fileid)), # sentences
			"vocab": len(set(word.lower() for word in gutenberg.words(fileid))) # unique words
		}
	return ret

if __name__ == "__main__":
	main()