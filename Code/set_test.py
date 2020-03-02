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
        self.assertCountEqual(set1.union(set2).hash.values(), ['A', 'B', 'D', 'E', 'G', 'I', 'W', 'X', 'Y', 'Z'])  # Item order does not matter
        self.assertCountEqual(set1.union(set3).hash.values(), ['C', 'M', 'N', 'V', 'W', 'X', 'Y', 'Z'])  # Item order does not matter

    def test_intersection(self):
        elements = ['2', 'A', 'B', 'C']
        elements2 = ['0', 'A', 'C', 'E', 'X', '2']
        elements3 = ['B', 'J', 'L', 'K', 'C', '2']
        set1 = HashSet(elements)
        set2 = HashSet(elements2)
        set3 = HashSet(elements3)
        self.assertCountEqual(set1.intersection(set2).hash.values(), ['A', 'C', '2'])  # Item order does not matter
        self.assertCountEqual(set1.intersection(set3).hash.values(), ['B', 'C', '2']) # Item order does not matter

    def test_difference(self):
        elements = ['5', '6', '8', '10', '1']
        elements2 = ['1', '5', '6', '7', '2', '9']
        elements3 = ['2', '4', '6', '9', '10']
        set1 = HashSet(elements)
        set2 = HashSet(elements2)
        set3 = HashSet(elements3)
        self.assertCountEqual(set1.difference(set2).hash.values(), ['8', '10'])  # Item order does not matter
        self.assertCountEqual(set1.difference(set3).hash.values(), ['5', '8', '1'])  # Item order does not matter

    def test_is_subset(self):
        elements = ['A', 'G', 'R']
        elements2 = ['G', 'D', 'R', 'P', 'A', 'W']
        elements3 = ['I', 'O', 'S', 'K', 'M', 'Z']
        set1 = HashSet(elements)
        set2 = HashSet(elements2)
        set3 = HashSet(elements3)
        assert set1.is_subset(set2) is True
        assert set1.is_subset(set3) is False
        assert set2.is_subset(set3) is False


if __name__ == '__main__':
    unittest.main()