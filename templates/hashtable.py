#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        # total of 8 linked lists
        self.buckets = [LinkedList() for i in range(init_size)]


    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'


    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))


    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)


    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys


    def values(self):
        """Return a list of all values in this hash table"""
        # TODO: Collect all values in each of the buckets
        list_of_values = []  
        for element in self.buckets:
            for linked_key, value in element.items():
                list_of_values.append(value)
        return list_of_values


    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items


    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        # TODO: Count number of key-value entries in each of the buckets
        count = 0
        # iterate through every key in this bucket
        for bucket in self.buckets:
            # use linkedList items() implementation to iterate through each item
            for data in bucket.items():
                # increment count for each item
                count += 1
        return count


    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # TODO: Check if the given key exists in a bucket    
        # get the keys, then iterate through each key element
        for element in self.keys():
            # check is element key is equal to key
            if element == key:
                return True
        return False


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # TODO: Check if the given key exists and return its associated value
        # checks if the key in valid
        if self.contains(key):   
            # iterate through each key element in each bucket
            for element in self.buckets:
                # use the linkedlist items method, get key value pairs
                for linked_key, value in element.items():
                    # if keys are equal, return the value of the matched key
                    if key == linked_key:
                        return value
        raise KeyError                    


    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # TODO: Insert or update the given key-value entry into a bucket

        # check if bucket contains key to set
        if self.contains(key):
            # delete the bucket if it contains an existing hash key
            self.delete(key)
        # determining the hash key, append the key value as a node element
        self.buckets[self._bucket_index(key)].append((key, value))


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # TODO: Find the given key and delete its entry if found
        if self.contains(key):
            # TODO -- check number of elements before deleting
            elements = self.buckets[self._bucket_index(key)].delete( (key, self.get(key)))
        else:
            # throw key error if no matching keys found
            raise KeyError


def test_hash_table():
    ht = HashTable()
    print(ht)

    print('Setting entries:')
    ht.set('I', 1)
    ht.set('I', 1)
    # print(ht)
    ht.set('V', 5)
    # print(ht)
    ht.set('X', 10)
    # print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('length: ' + str(ht.length()))
    print(ht.values())

    # Enable this after implementing delete:
    # print('Deleting entries:')
    # ht.delete('I')
    # print(ht)
    # ht.delete('V')
    # print(ht)
    # ht.delete('X')
    # print(ht)
    # print('contains(X): ' + str(ht.contains('X')))
    # print('length: ' + str(ht.length()))


if __name__ == '__main__':
    test_hash_table()
