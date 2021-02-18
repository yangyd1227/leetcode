Hash table is the optimization here.

To check if an element is in hash table key, we can do in O(1) by checking if ```dict[key]``` gives an error, as accessing an element is O(1) for hash tables.
In python, dict.keys() creates the whole list of keys, so it is an O(N) operation, while key in dict is an O(1) operation.

"
The in operator, like most other operators, is just a call to a __contains__ method (or the equivalent for a C/Java/.NET/RPython builtin). list implements it by iterating the list and comparing each element; dict implements it by hashing the value and looking up the hash; blist.blist implements it by walking a B+Tree; etc. So, it could be O(n), O(1), O(log n), or something completely different.
"
