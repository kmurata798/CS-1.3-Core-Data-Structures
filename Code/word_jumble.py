# SOLUTION OPTIONS:
# Word Jumble Unscrambler: Binary tree attempt
# 1. Sorted array + Vinary search
# 2. Binary Search Tree
# 3. Permutations
# 4. Dictionary Lookups ==> word_jumble_sort.py
# 5. Sets
# 6. Combinations
# 7. Anagram Trie (Prefix Trie)

from binarytree import BinarySearchTree, BinaryTreeNode


# String we want to unscramble
scrambled = ['lbal']

# Helper functions to FILTER DOWN DICTIONARY WORDS
# Search for all words in python dictionary that have the same length of letters as the scrambled string
def filter_dict_string_length(scrambled_string):
    for index in python_dictionary():
        for i in scrambled_string:
            if len(index) == len(i):
                print(index)
# find words that include share double letters, if scrambled word includes double letters
# def matching_chars(scrambled_string)

# Grabs all words from BUILT IN PYTHON DICTIONARY
def get_file_lines(filename):
    '''OPEN the FILE _WITHIN_ a function, you DON'T HAVE TO TYPE file.close()!!!!!'''
    with open(filename, "r") as f:
        lines = f.readlines() 
        strip_line = [word.strip() for word in lines]
    return strip_line

def python_dictionary():
    lines = get_file_lines("/usr/share/dict/words")
    # print(lines)
    return lines

if __name__ == '__main__':
    # python_dictionary()
    filter_dict_string_length(scrambled)