#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))

class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        """ O(n) """
        self.head = None # O(1)
        self.tail = None # O(1)
        if iterable: # O(1)
            for item in iterable: # O(n)
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list"""
        items = ['({})'.format(repr(item)) for item in self.items()] # O(n)
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list"""
        result = [] # O(1)
        current = self.head # O(1)
        while current is not None: # O(n)
            result.append(current.data) # O(1)
            current = current.next # O(1)
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None # O(1)

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # set the current count of items to 0 
        count = 0 # O(1)
        # set the Node object to start of list, i.e. head
        current = self.head # O(1)
        # loop through the linked_list, beginning with head node
        while current is not None: # O(n)
            # increment the item count
            count += 1 # O(1)
            # set the current count to next node in linkedlist
            current = current.next # O(1)   
        # return the count as length
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # creates a new node instance with given item as node data
        node = Node(item) # O(1)
        # sets the next node as head when the list is empty
        if self.is_empty(): # O(1)
            # assign node as the head, and the tail in step below
            self.head = node # O(1)
        else:
            # set the next node to current node
            self.tail.next = node # O(1)
        # always set node to tail - per append case
        self.tail = node # O(1)

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # creates a new node instance with given item as node data
        node = Node(item) # O(1)
        # set the next node as tail, if empty
        if self.is_empty(): # O(1)
            # assign node as tail, and head in step below
            self.tail = node # O(1)
        else:
            # insert node as head, if not tail
            node.next = self.head # O(1)
        # always set node to head - per prepend case
        self.head = node # O(1)      


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found
        # set the current variable to head node of this linked list
        current = self.head # O(1)
        # initialize a veriable to store the previous node, can be head, tail or previous
        previous = None # O(1)
        # initialize variable to capture the reference node to delete
        found = False # O(1)
        # search for item, starting a the current node, head in this case
        while not found and current is not None:  # O(n)
            # when the current the search item, set found to true to break the loop
            if current.data == item: # O(1)
                found = True # O(1)
            else:
                # keep tabs, store, the previous and next node of this linked list
                previous = current # O(1)
                current = current.next # O(1)

        # when item is found, reassign the node pointer
        if found: # O(1)
            # handle pointer relocation for items to delete after head or before tail
            if current is not self.head and current is not self.tail: # O(1)
                # moves the previous pointer +1, so this current.next can be deleted
                previous.next = current.next # O(1)
                # this current.next is set to None, deleted
                current.next = None # O(1)
            # when current is head
            if current is self.head: # O(1)
                # set the head to next node
                self.head = current.next # O(1)
                # delete this current.next value, set to none
                current.next = None # O(1)
            # when current is not self.tail
            if current is not self.tail: # O(1)
                # reset the tail to previous
                if previous is not None: # O(1)
                    previous.next = None # O(1)
                self.tail = previous # O(1)   
        else:
            raise ValueError('Item not found: {}'.format(item))      


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # find item where quality(item) is True

        # set current to head of this linked list
        current = self.head # O(1)
        # when this linked list has nodes
        while current is not None:  # O(n)     
            # when the quality is the current data, return it 
            if quality(current.data): # O(1)
                return current.data # O(1)
            # otherwise, set the current to the next node
            current = current.next # O(1)    


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('length: ' + str(ll.length()))

    # Enable this after implementing delete:
    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('length: ' + str(ll.length()))


if __name__ == '__main__':
    test_linked_list()
