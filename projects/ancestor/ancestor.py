from util import Stack, Queue
from collections import deque
from graph import Graph
from collections import defaultdict	

# ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


# def earliest_ancestor(ancestors, starting_node):
# 	queue = deque()
# 	queue.append(starting_node)
# 	relationship = {}
	
# 	for ancestor in ancestors: 
# 		parent, child = ancestor[0], ancestor[1] # Sets 0 and 1 index to respective parent and child variables.

# 		if child not in relationship: # If 1 index not in the relationshop dictionary, relationship key is the child/0 index.
# 			relationship[child] = set() # This sets the dictionary value to an empty set().
# 		relationship[child].add(parent) # Adds the parent index 0 to the dictionary value
		
# 	print('Myne', relationship)


	
	

# # print('Targeted', ancestors[8])
# print('')
# print('Ancestor', earliest_ancestor(ancestors, 9))
# print('')
# # Earliest known ancestor will have the longest path
# # If more than one ancestor, return the one with the lowest numberic ID/value.
# # Return -1 if there no parents exist. 


