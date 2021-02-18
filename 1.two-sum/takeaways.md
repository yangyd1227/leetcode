Hash table is the optimization here.

To check if an element is in hash table key, we can do in O(1) by checking if dict[key] gives an error, as accessing an element is O(1) for hash tables.
In python, dict.keys() creates the whole list of keys, so it is an O(N) operation, while key in dict is an O(1) operation.
