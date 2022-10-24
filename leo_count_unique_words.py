#!/usr/bin/env python
from collections import defaultdict
import sys
import time

punctuation_characters = "~`!@#$%^&*()_-+=[{]}\|;:',<.>/?1234567890"

def strip_word(word):
    return "".join([x for x in word if x not in punctuation_characters]).strip('\"').lower()

def count_words_dictionary(file_name):
    dictionary = defaultdict(int)
    for word in open(file_name).read().split():
        dictionary[strip_word(word)] += 1
    del dictionary['']
    return len(dictionary)

def count_words_set(file_name):
    with open(file_name, "r") as file_id:
        lines = file_id.read().splitlines()
        uniques = set()
        for line in lines:
            uniques |= set(strip_word(m) for m in line.split())
    uniques.remove('')
    return len(uniques)


if len(sys.argv) < 1:
    print('Usage:')
    print('     python ' + sys.argv[0] + ' file_name')
    print('Please specify the file name')
    sys.exit()

def main():
    file_name = sys.argv[1]
    t0 = time.perf_counter()
    n = count_words_dictionary(file_name)
    t1 = time.perf_counter()
    n = count_words_set(file_name)
    t2 = time.perf_counter()
    print(t1-t0,t2-t1,sep="\n")

if __name__ == "__main__":
    main()