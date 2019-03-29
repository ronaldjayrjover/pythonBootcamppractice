'''
zip
    imagine we have 2 list of numbers with exact lenght that it will pair up the 2 list

'''
# first_zip = zip([1,2,3], [4,5,6]) #tuple
# #print(list(first_zip)) #need to comment kasi sinisira naka join na as converted to a list
#                         #[(1, 4), (2, 5), (3, 6)]
# print(dict(first_zip)) # {1: 4, 2: 5, 3: 6}
#
# nums1 = ([1,2,3,4,5])
# nums2 = ([6,7,8,9,10])
# strings = ("hi", "hello", "whats", "up")
#
# l = zip(nums1, nums2)
# print(list(l))
#
# z = zip(nums1, nums2, strings)
# print(list(z))
#
# k = zip(strings, nums2, nums1)
# print(list(k))
#
# nums3 = [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
# u = list(zip(*nums3)) # if we pass * it will take each element from each tuple and pair up to create a tuple
# print(u)  # [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)]
#
# print(#### complexx zip####)

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']


# returns dict with {student:highest score} USING DICT COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades1 = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}
print(final_grades1)

# returns dict with {student:highest score} (same thing as above) USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades2 = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)
print(final_grades2)
# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0]+pair[1])/2),
            zip(midterms, finals)
        )
    )
)

