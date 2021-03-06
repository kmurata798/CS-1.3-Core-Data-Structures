#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing.
    
    time complexity: O(1)"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    """time complexity: O(n) because your must loop through each word starting from both ends of the string, until you reach the middle"""
    extra = " ?!,.;:-_'"
    for index in extra:
        text = text.replace(index, '')
    first_pt = 0
    second_pt = len(text) - 1
    if len(text) < 1:
        return True

    while first_pt <= second_pt:
        if text[first_pt].lower() != text[second_pt].lower():
            return False
        first_pt += 1
        second_pt -= 1
    return True



def is_palindrome_recursive(text, left=None, right=None):
    """time complexity: O(1) because you are checking which conditional will run, which does not involve any loops
    text = str
    left = int
    right = int"""
    if len(text) == 0:
        return True
    given = get_letters(text)
    if left is None and right is None:
        left = 0
        right = len(str) - 1

    if given[left] != given[right]:
        return False
    elif left >= right:
        return True
    else:
        return is_palindrome_recursive(given, left+1, right-1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
