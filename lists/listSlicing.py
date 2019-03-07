#some_list[start:end:step]

#first_list = [1, 2, 3, 4]
#print(first_list[1:])
##start and end
colors = ['red', 'orange', 'blue', 'green', 'yellow']
print(colors[2])
print(colors[2:])
print(colors[1:3])
print(colors[1:4])
print("------------------------break-------------------------------")
#third parameter for slice is step
first_list = [1, 2, 3, 4, 5, 6]
print(first_list[1::2])
print(first_list[::2])
print(first_list[1::-1])
colors = ['red', 'orange', 'blue', 'green', 'yellow']
print(colors[::2])
print(colors[::-1])
print(colors[4][::-1])
print("------------------------break-------------------------------")
#swapping values ### use for shuffling and sorting

names = ['James', 'Michelle']
names[0], names[1] = names[1], names[0]
print(names)

