from set import HashSet
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        elements = ['1', '2', '3']
        set = HashSet(elements)
        assert set.size is 3

    def test_size(self):
        elements = ['A', 'B', 'C', '1', '2']
        set = HashSet(elements)
        assert set.size is 5
    
    def test_contains(self):
        elements = ['K', 'Q', 'J', 'O']
        set = HashSet(elements)
        assert set.contains('K') is True
        assert set.contains('J') is True
        assert set.contains('Q') is True
        assert set.contains('C') is False
        assert set.contains('W') is False

    def test_add(self):
        elements = ['R', 'V']
        set = HashSet(elements)
        set.add('M')
        set.add('T')
        with self.assertRaises(KeyError):
            set.add('M')  # Element already exists
        with self.assertRaises(KeyError):
            set.add('V')  # Element already exists
        assert set.size is 4
        assert set.contains('R') is True
        assert set.contains('T') is True

if __name__ == '__main__':
    unittest.main()