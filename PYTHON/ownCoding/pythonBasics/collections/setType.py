#set in python
thisset = {"apple", "banana","cherry" }
print(thisset)

#Length of a set:
print(len(thisset))
# it is possible that a set has different datatypes: int, str, float,...

print(type(thisset))

#set constructor: set()
myset = set(("apple", "cucumber"))

#joining two or more sets together:
#newset= (thisset) + (myset)
#print(newset)

newset = myset | thisset
print(newset)

newset = thisset.union(myset)
print(newset)