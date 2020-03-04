from hashtable import HashTable
# from binarytree import BinarySearchTree, BinaryTreeNode

class HashSet:
    def __init__(self, elements=None):
        """initialize a new empty set structure, and 
        add each element if a sequence is given"""
        self.hash = HashTable()
        self.size = 0
        if elements != None:
            for element in elements:
                self.add(element)
    
    def size(self):
        """Property that tracks the number of elements in constant time.
        Runtime complexity: O(1) since we are constantly keeping track of the size everytime we add/remove an item.
        """
        return self.size

    # def __contains__(self, item):
    #         ''' Special method allowing use of `in` '''
    #         return item in self.table

    # def __iter__(self):
    #     ''' Special method allowing use of looping. '''
    #     for item in self.table.items():
    #         yield item

    def contains(self, element):
        """return a boolean indicating whether element is 
        in this set.
        Average case Rrntime complexity: O(1) since hashtable contains() function needs to find bucket index and traverse it's nodes to find the target element.
        """
        return self.hash.contains(element)
    
    def add(self, element):
        """add element to this set, if not present already.
        Average runtime complexity: Average case O(1) since hashtable contains() function needs to find bucket index and traverse it's nodes to find the target element.
        Worst case runtime complexity: O(n) if we need to resize the hashtable due to load factor exceeding its efficient limit.
        """
        if self.contains(element):
            raise KeyError(f"Cant add element to set more than once: {element}")
        else:
            self.hash.set(element, element)
            self.size += 1
    
    def remove(self, element):
        """remove element from this set, if present, 
        or else raise KeyError.
        Average case runtime complexity: O(1) since hashtable contains() function needs to find bucket index and traverse it's nodes to find the target element.
        Worst case runtime complexity: O(n) if we need to resize the hashtable if the load factor would benefit from reducing the size of the hashtable.
        """
        if self.contains(element):
            self.hash.delete(element)
            self.size -= 1
        else:
            raise KeyError(f"The element doesnt exist in the set: {element}")

    # def __len__(self):
    #     ''' Special method allowing use of `len()`. '''
    #     return self.size

    def union(self, other_set):
        """return a new set that is the union of this set 
        and other_set.
        Average case runtime complexity: O(n(1) + n(2)) because we are looping through both sets, and adding them together, excluding duplicates. We use n1 and n2 since
                                            each set may have different sizes.
        """
        new_set = HashSet()
        for element in self.hash.values():
            new_set.add(element)
        # Add the other_set elements, avoiding duplicates
        for element in other_set.hash.values():
            if not new_set.contains(element):
                new_set.add(element)
        return new_set
        
    # def _smaller_larger_check(self, set1, set2):
    #     if len(set1) > len(set2):
    #         return set2, set1
    #     return set1, set2
            
    def intersection(self, other_set):
        """return a new set that is the intersection of 
        this set and other_set.
        Average case runtime complexity: O(m) where m is the smaller sized set. This is because we are looping through each element in the set.
        """
        # smaller, larger = self._smaller_larger_check(self, other_set)
        new_set = HashSet()
        for element in self.hash.values():
            if other_set.contains(element):
                new_set.add(element)
        # for element in smaller:
        #     if element in larger:
        #         new_set.add(element)
        return new_set

    def difference(self, other_set):
        """return a new set that is the difference of 
        this set and other_set.
        Average case runtime complexity: O(n) since we are looping through each element in self set. 
        """
        new_set = HashSet()
        for element in self.hash.values():
            if not other_set.contains(element): # Check if the element does not exist in the other_set.
                new_set.add(element)
            # If element does exist in other_set, then don't add element and loop to the next one.
        return new_set
        
    def is_subset(self, other_set):
        """return a boolean indicating whether other_set 
        is a subset of this set.
        Best case runtime complexity: O(1) if the self set is bigger than the other_set.
        Average case runtime complexity: O(n) if self set is smaller than the other_set, where we would loop through all the elements in the set to check if 
                                            all elements exist in other_set.
        """
        if self.size > other_set.size:
            return False
        else:
            count = 0
            for element in self.hash.values():
                if other_set.contains(element):
                    # increment count variable everytime a matching element is found in other_set.
                    count += 1
            # return bool for whether the size of self set matches the number of elements matching in other_set.
            return self.size == count

def test_set():
    elements1 = ['A', 'B', 'C', 'G']
    elements2 = ['A', 'B', 'C', 'E', 'G']
    set1 = HashSet(elements1)
    set2 = HashSet(elements2)
    print(set1.union(set2).hash.values())
    print(set1.intersection(set2).hash.values())
    print(set1.difference(set2).hash.values())
    print(set1.is_subset(set2))

if __name__ == '__main__':
    test_set()


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
        # new_set = Set()
        