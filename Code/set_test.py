from set import HashSet
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        elements = ['1', '2', '3']
        set = HashSet(elements)
        assert set.size is 3

if __name__ == '__main__':
    unittest.main()