x = frozenset([23,19,49,25,34])
y = frozenset([10,36,34,28,19])
 
print(x.isdisjoint(y))

print(x.difference(y))

print(x | y)