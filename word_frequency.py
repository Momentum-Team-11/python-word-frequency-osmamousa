STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    pass
file = open("../Python/praise_song_for_the_day")

import string

#Comb every line, remove punctuations and replace withe empty string
def strip_punctuations(line):
    for charachter in string.punctuation:
        line = line.replace(charachter,"")
        return line

#too keep things uniform we must make all words lowercase
#we assign each word as a key and assign value givin the ammount of times that key was displayed
#Add one to the word key everytime it appears
with open(file, 'r') as fi:
    line = strip_punctuations(line)
    words = line.split()
    for word in words:
        word = word.lower()
        if word not in word_count:
            word_count[word] = 0
    word_count[word] += 1

list(word_count.keys())

word_list = list(word_count.keys)
for word in word_list:
    print(word,word_count[word])

#order the dict by frequency
#and sort
def order_dict_by_freq(dictionary):
    sorted_values = []
    for key in dictionary:
        sorted_values.append((dictionary[key],key))
    sorted_values = sorted(sorted_values)
    sorted_values = sorted_values[::-1]
    return sorted_values

#lets do this with the whole list
word_list = order_dict_by_freq(word_count)
for tuple_freq in top_words:
    count, word = tuple_freq
    print(word, count)



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
