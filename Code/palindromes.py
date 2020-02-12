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
    """time complexity: O(n)"""
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

    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    """time complexity: O(n)
    text = str
    left = int
    right = int"""
    # if left == None:
    #     left = 0
    #     right = len(text) - 1
    #     extra = " ?!,.;:-_'"
    #     for index in extra:
    #         text = text.replace(index, '')
    # if left < right and right <= len(text) - 1:
    #     if text[left].lower() != text[right].lower():
    #         return False
    #     is_palindrome_recursive(text, left+1, right-1)
    # if len(text) < 1:
    #     return True
    # return True
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
    
        
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


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
