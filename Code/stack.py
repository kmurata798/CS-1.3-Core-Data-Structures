#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if self.list.length() == None:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        # self.list.length()
        self.list.size() # 0(1) runtime

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) direct access to the top item"""
        # TODO: Push given item
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if not self.is_empty():
            return self.list.tail.data
        return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) directly remove top item"""
        # TODO: Remove and return top item, if any
        if self.is_empty():
            raise ValueError("Empty Queue!")

        top = self.list.tail.data
        self.list.delete(top)
        return top


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        if not self.list:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this stack."""
        # Count number of items
        return len(self.list)


    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) direct access to head"""
        # Insert given item
        # self.list.append(item) # add item to end of list
        self.list.insert(0, item) # add item to beginning of list

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        if not self.list:
            return None
        else:
            # return self.list[self.length() - 1] # look at last item of list
            return self.list[0] # look at first item in list

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) directly remove top item"""
        # Remove and return top item, if any
        if len(self.list) > 0:
            # temp = self.list[self.length() - 1]
            # self.list.pop(self.length() - 1)
            temp = self.list[0]
            self.list.pop(0)
            return temp
        else:
            raise ValueError
        


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
