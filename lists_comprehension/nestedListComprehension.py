nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print([[print(val) for val in i] for i in nested_list])

board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)

print([["X" if num % 2 != 0  else "O" for num in range(1,4)] for val in range(1,4)])

'''
Using a nested list comprehension and range(), create a variable called answer with the following value - 
[[0,1,2],[0,1,2], [0,1,2]]. Start by using range and a list comp to generate the list[0,1,2] and then repeat that whole thing
3 times in a nested list comp
'''
answer = [[num for num in range(0,3)] for num in range(0,3)]
print(answer)

