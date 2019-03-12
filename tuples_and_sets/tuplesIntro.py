#an ordered collection
#an immutable list - can never be changed

alphabet = ('a', 'b', 'c', 'd')

months = ( 'Jan', 'Feb', 'Mar',
            'Apr', 'May', 'Jun',
           'Jul', 'Aug', 'Sept',
           'Oct', 'Nov', 'Dec'
)

locations = {
    (35.6, 39.69): "Tokyo",
    (37.6, 40): "New York",
    (33, 37): "San Francisco",
}
print(locations[(35.6, 39.69)])
cat = {
    "name": "biscuit",
    "age": 0.5,
    "favorite": "chap"
}
print(cat)
print(cat.items())


###### Tuples iterating #######

#for months in months:
#    print(months)

i = len(months) - 1
while i >= 0:
    print(months)
    i -= 1

