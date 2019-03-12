##sets - formal mathematical sets. do not have duplicate values. elemetns in sets aren't ordered.
#you cannot access items in a set by index.
#can be useful if you need to keep track of a collection of elements, but dont care about ordering, keys or values and duplicates

s1 = set({1,2,3,4,5,5,5})
print(s1)

s2 = set({1,2,3,4})
print(s2)

print(4 in s1)
print(5 in s2)

#for thing in s1:
#    print(thing)

s3 = {'a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'r'}

print(set(s3))
print(len(set(s3)))

###### Set Methods ########
#add
s1.add(6)
print(s1)
#remove
s2.remove(4)
print(s2)
#copy
s4 = s3.copy()
print(s4)
#clear
s4.clear()
print(s4)

## | and & sets
set6 = {'ab', 'cd', 'ef', 'gh', 'ij'}
set7 = {'cd', 'mn', 'op', 'qr'}
print(set6 | set7) # union and if may same, only 1 entry
print(set6 & set7) # cd ang same

