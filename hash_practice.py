
# this creates an empty hash table having empty lists
hashmap = [ [] for bucket in range(256) ]
print(hashmap)

# use pythons hash function to generate a numeric key
hash_key = hash('06770') 
print('Hashmap: {} '.format(hash_key))

# use pythons hash function with length of hashmap to generate a deterministic key
hash_key = hash('06770') % len(hashmap)
print('Hashmap With len(): {} '.format(hash_key))

# now with a deterministic key, insert the tuple at the given key location
hashmap[hash_key].append( ('06770', 'Minneapolis MN') )
hashmap[hash_key].append( ('06403', 'St. Louis MO' ) )
print(hashmap)

print(hashmap[hash_key][1])

