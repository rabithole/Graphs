from util import Stack, Queue
from collections import deque
from graph import Graph
from collections import defaultdict	

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def earliest_ancestor(ancestors, starting_node):
	queue = deque()
	queue.append(starting_node)
	relationship = {}
	temp = {}
	for ancestor in ancestors:
		if ancestor[0] in relationship:
			# print('In relationship')
			relationship[ancestor[0]] = {temp, ancestor[1]}
			temp = ancestor[1]
			# print('Relationship', relationship)
		else:
			# print('Not in relationship')
			temp = ancestor[1]
			relationship[ancestor[0]] = {ancestor[1]}
		
	print(relationship)


	
	

# print('Targeted', ancestors[8])
print('')
print('Ancestor', earliest_ancestor(ancestors, 9))
print('')
# Earliest known ancestor will have the longest path
# If more than one ancestor, return the one with the lowest numberic ID/value.
# Return -1 if there no parents exist. 
