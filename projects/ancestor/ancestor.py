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

ancestors = {
	11: {},
	10: {},
	9: {8},
	8: {4, 11},
	7: {5},
	6: {3, 5},
	5: {4},
	4: {},
	3: {1, 2},
	2: {},
	1: {10}
}


def earliest_ancestor(ancestors, starting_node):
	
	
	if ancestors[starting_node]:
		print('These are your ancestors!', ancestors[starting_node])

	else: 
		print('No ancestors', ancestors[starting_node])

# print('Targeted', ancestors[8])
print('')
earliest_ancestor(ancestors, 6)
print('')
# Earliest known ancestor
# If more than one ancestor, return the one with the lowest numberic ID/value.
# Return -1 if there are no parents exist. 