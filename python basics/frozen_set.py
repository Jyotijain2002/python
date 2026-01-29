# frozenset :  is an immutable version of a set.
# Like sets, it contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset.

#creating frozenset: use frozenset constructor to create forzenset from any iteratable
f1=frozenset({1,2,3})
print(f1)
print(type(f1))

# frozenset methods
f2=f1.copy() # returns a shallow copy of f1
print(f2)

fa=frozenset({1,2,3,4})
fb=frozenset({5,3,4,8,9})

x=fa-fb # or you can use difference() method
print(x)

y=fa & fb # or use intersection() method
print(y)

print(fa.isdisjoint(fb)) # False
print(fa.issubset(fb)) # False
print(fa.issuperset(fb)) # False

z=fa^fb # or use symmetic_difference() method
print(z)

p=fa|fb # or use union() method
print(p)
