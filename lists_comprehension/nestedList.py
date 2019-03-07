#a list inside a list
#lisrs can contain any kind of element, even other lists
#used on complex data structures - matricies, game boards / mazes, rows and columns for virtualizations,tabulation
#and grouping data

#Accessing nested list
accessing_list = [[1,2,3],[4,5,6],[7,8,9]]
print(accessing_list[0][1]) # first list and index 1
print(accessing_list[1][2]) # second list and index 2
print(accessing_list[-1][0]) # reverse list meaning the last list and index 1

nested_list = [[1,2,3],[4,5,6],[7,8,9]]

for i in nested_list: # main list then going throug inside list
    for val in i: # val in now the inside list
        print(val) # now printing it


