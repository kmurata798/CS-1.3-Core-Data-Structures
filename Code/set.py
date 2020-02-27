from hashtable import HashTable
# from binarytree import BinarySearchTree, BinaryTreeNode

class HashSet:
    def __init__(self, elements=None):
        self.hash = HashTable()
        self.size = 0

    def contains(self, element):
        return self.hash.contains(element)
    
    def add(self, element):
        if self.contains(element):
            return self.hash.set(element, element)
            self.size += 1
    
    def remove(self, element):
        if self.contains(element):
            return self.hash.delete(element)
            self.size -= 1

    def union(self, other_set):
        
    def intersection(self, other_set):
        
    def difference(self, other_set):
        
    def is_subset(self, other_set):
        


# class TreeSet:
#     def __init__(self, elements=None):
#         self.tree = BinarySearchTree()
#         if elements is not None:
#             for element in elements:
#                 self.add(element)
    
#     def contains(self, element):
#         return self.tree.contains(element)

#     def add(self, element):
#         if self.contains(element):
#             raise ValueError(f'Cannot add element to set again: {elemenet}')
#         else:
#             self.tree.insert(element)
    
#     def intersection(self, other_set):
#         new_set = Set()
#         def __init__(self, *args, **kwargs):
#             super(for element in self.tree.iteems_in_order():
#             if other_set.contains(element):
#                 new_set.add(element)
#         return new_set
    
#     def union(self, other_set):
        new_set = Set()
        