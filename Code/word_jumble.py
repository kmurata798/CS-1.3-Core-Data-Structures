from binarytree import BinarySearchTree, BinaryTreeNode

def get_file_lines(filename):
    '''OPEN the FILE _WITHIN_ a function, the you DON'T HAVE TO TYPE file.close()!!!!!'''
    with open(filename, "r") as f:
        lines = f.readlines() 
        strip_line = [word.strip() for word in lines]
    return strip_line

def python_dictionary():
    lines = get_file_lines("/usr/share/dict/words")
    print(lines)

if __name__ == '__main__':
    python_dictionary()