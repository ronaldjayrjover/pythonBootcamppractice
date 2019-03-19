'''
in our functions we put first:
1.parameter/s then
2. *args
3. default parameters
4. **kwargs

'''

#sample
def display_info(a,b, *args, instructor="jay", **kwargs):
    return [a, b, args, instructor, kwargs]
print(display_info(1,2,3, last_name="jover", job='instructor'))

# a = 1
# b = 2
# args = (3,) ##tuples
# prints instructor - "jay"
# kwargs {'last_name': "jover", "job": "instructor"}


'''
Asnwer from the terminal: 

/Users/ronaldj/Documents/pythonbootcamp/pythonBootcamppractice/converge/bin/python /Users/ronaldj/Documents/pythonbootcamp/pythonBootcamppractice/functions_part2/parameterOrdering.py
[1, 2, (3,), 'jay', {'last_name': 'jover', 'job': 'instructor'}]

Process finished with exit code 0
'''