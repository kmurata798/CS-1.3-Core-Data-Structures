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

    def test_remove(self):
        elements = ['Z', 'I', 'Q', '4', 'S']
        set = HashSet(elements)
        with self.assertRaises(KeyError):
            set.remove('A')  # Element doesn not exist
        with self.assertRaises(KeyError):
            set.remove('X')  # Element does not exist
        set.remove('Z')
        set.remove('4')
        assert set.contains('Z') is False
        assert set.contains('4') is False
        with self.assertRaises(KeyError):
            set.remove('Z')  # Element does not exist anymore

    def test_union(self):
        elements = ['W', 'X', 'Y', 'Z']
        elements2 = ['A', 'B', 'D', 'E', 'G', 'I']
        elements3 = ['C', 'V', 'M', 'N']
        set1 = HashSet(elements)
        set2 = HashSet(elements2)
        set3 = HashSet(elements3)
        self.assertCountEqual(set1.union(set2).hash.values(), ['A', 'B', 'D', 'E', 'G', 'I', 'W', 'X', 'Y', 'Z'])  # item order does not matter
        self.assertCountEqual(set1.union(set3).hash.values(), ['C', 'M', 'N', 'V', 'W', 'X', 'Y', 'Z'])  # Item order does not matter

if __name__ == '__main__':
    unittest.main()