##########################################################################
# TUPLE: Immutable, index, negative indexed to access from the end. 
# Can change other data types inside the tuple.

my_tuple = ('p', 'r', 'i', 'n', 'y', [1, 2, 3, 4],  'a', 'a')

## Slicing: 
print(my_tuple[1:4])
print(my_tuple)

## Nested indexing 
print(my_tuple[5][2])

## Negative indexed. Access from end. 
print(my_tuple[-1]) # Last time is an 'a'

## Tuple methods
### Count, counts the number of times an element occurs in the tuple. 
print(my_tuple.count('a'))
print(my_tuple.count('p'))

### Index: Returns the index of the element requested
print(my_tuple.index([1, 2, 3, 4]))

### Tuple will return a bolean when checking to see if the element exists in the tuple. 
print('a' in my_tuple, 'x' in my_tuple)




#############################################################################
# STRING: Indexed, negative indexed, slicing, immutable with slicing, iterable
### Can check if a character or group of characters exists within a string. 

### String methods
# enumerate(), len(), format()
# split(), .lower(), .upper(), .join(), .find(), .replace()

word = 'wordsy'
print(len(word), list(enumerate(word)))
print(enumerate(word)) # Without list() enumerate returns an object

print('\x62') # Prints the letter the code coresponds to. 


#############################################################################
# Refer here for a full list of set() methods. https://www.programiz.com/python-programming/set
# SETS: All elements are unique. (No duplicates) Mutable, not indexed
### Items in a set are immutable. The set itself can be changed. In other words, items can be added and removed from the set. 
# Initializing a set below. 
my_set = set() # This creates an empty set. 
print('My set', my_set)

### Set methods
my_set.update([2, 4, 7])
my_set.add(5)
# my_set.remove()
# my_set.discard()
# my_set.clear() clears the set()
print(my_set)
print('Pop()', my_set.pop())


print('My set', my_set)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print('AB', A | B)  # | = union operator

# Union() method
print('Union()', A.union(B))

# Set intersection. Returns the common elements
print('AB intersection', A & B)
print('Intesection()', A.intersection(B))

# Set difference
print('A not B', A-B) # Prints or returns what is in A but not in B. 
print('A difference()', A.difference(B))

# Set symmetric difference
print('Symmetric difference', A^B)
print('symmetric_differnce()', A.symmetric_difference(B))