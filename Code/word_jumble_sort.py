# Word Jumble Unscrambler: Using sorted Python Dictionary

def create_dict():
    """Create a dictionary with keys of sorted letters (alphabetized) and a value that is a list of words that are that sorted word."""
    # empty dictionary that we will input key value entries based off the computer's dictionary
    dictionary = {}
    # open the built in dictionary existing in Mac computers
    with open("/usr/share/dict/words", "r") as f:
        # loop through each word in the computer's dicitonary
        for word in f:
            # .strip() removes any leading/trailing spaces in each word + .lower() turns all characters to lower cased
            word = word.strip().lower()
            # sort the letters of each word alphabetically
            sorted_word = ''.join(sorted(word))
            # create an entry with the sorted word as key and new dict as value, or append the word to the entry that already exists
            # setdefault() returns the value of a key, sorted_word (if it is in dictionary). If key does not exist, it inserts key with a value to the dictionary.
            dictionary.setdefault(sorted_word, []).append(word)
    # return the new dictoonary
    return dictionary

def unscramble_word(word):
    # sort the scrambled word so that we can look it up based on the alphabetical order
    sorted_input = ''.join(sorted(word)) 
    # Creates alphabetized dictionary
    sorted_dict = create_dict()
    # check if alphabetizd input string matches alphabetized computer dictionary words
    if sorted_input in sorted_dict:
        #if it does match a word, return the value existing in the key, sorted_input, from the dictionary
        return sorted_dict.get(sorted_input, []) # safer usage?
        # return sorted_dict[sorted_input]
    else:
        return None

def unscramble_words(words):
    # List to add unscrambled words to
    answers = []

    # loop through the given words
    for word in words:
        # unscramble the single scrambled word
        unscrambled_words = unscramble_word(word)
        # check to make sure there are words
        if unscrambled_words is not None:
            # if there is only one option for the given word
            if len(unscrambled_words) == 1:
                # add the single word to the answers array
                answers.extend(unscrambled_words)
            else:
                # add the full list of scrambled word options
                answers.append(unscrambled_words)
    # return the final answers word list
    return answers

if __name__ == "__main__":
    words = ['labl', 'thrsi', 'cipnci', 'yrpoopinutt', 'yfari', 'tabreleiot', "retgamel"] 
    # Answers ===> ball, shirt, picnic, opportunity, fairy, obliterate, telegram
    unscrambled_words = unscramble_words(words)
    print(unscrambled_words)