from util import Stack, Queue
from collections import deque

# children = {
# 	1: {3},
# 	2: {3},
# 	3: {6},
# 	4: {5, 8},
# 	5: {6, 7},
# 	6: {},
# 	7: {},
# 	8: {9},
# 	9: {},
# 	10: {1},
# 	11: {8}
# }

# ancestors = {
# 	11: {},
# 	10: {},
# 	9: {8},
# 	8: {4, 11},
# 	7: {5},
# 	6: {3, 5},
# 	5: {4},
# 	4: {},
# 	3: {1, 2},
# 	2: {},
# 	1: {10}
# }

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def earliest_ancestor(ancestors, starting_node):
	queue = deque()
	queue.append(starting_node)
	for ancestor in ancestors:
		parent = ancestor[0]
		child = ancestor[1]
		# print(parent, child)


	
	

# print('Targeted', ancestors[8])
print('')
earliest_ancestor(ancestors, 11)
print('')
# Earliest known ancestor will have the longest path
# If more than one ancestor, return the one with the lowest numberic ID/value.
# Return -1 if there no parents exist. 

