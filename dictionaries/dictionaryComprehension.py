#{ __:___ for __ in ___}
#iterates over keys by default
#to iterates overs keys and values by using .items()

numbers = dict(first=1, second =2, third=3)
squared = {key: value ** 2 for key,value in numbers.items()}
print(squared)

numbers2 = {num: num**2 for num in [1,2,3,4,5]}
print(numbers2)

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0,len(str1))}
print(combo)

#####

instructor = {
    "name": "jay",
    "age": 'thirtysix',
    "state": "quezon",
    "color": "blue"
}
yelling_instructor = {k.upper(): v.upper() for k,v in instructor.items()}
print(yelling_instructor)

###### conditonal logic with dictionaries

num_list = [1,2,3,4,5]
evenodd = {num:("even" if num % 2 == 0 else "odd") for num in num_list}
print(evenodd)
evenodd2 = {num:("even" if num % 2 == 0 else "odd") for num in range(1,200)}
print(evenodd2)

#using yelling instructor but having the k and v of COLOR to upper case (doing a condition on the left side of the
#dictionary comprehension
yelling_instructortwo = {(k.upper() if k is 'color' else k): v.upper() for k,v in instructor.items()}
print(yelling_instructortwo)