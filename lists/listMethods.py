#list method = append, insert and extend

data = [1,2,3]
data.append("purple") ### 1 item to the end of the list
print(data)
data.extend([4,5,6]) ### multiple item to the end of the list
print(data)
data.insert(4, "red") ### it will add after the index number of what you specified
print(data)
print("------------------------break-------------------------------")
#list method = clear, pop and remove
datas = [1,2,3]
datas.clear() #remove all item
print(datas)
datas = [1,2,3] # need to reinitialize again the variable as i cleared it
datas.pop(1) # removing an item base on the index you have specified
print(datas)
datas = [1,2,3,3,3,4]
datas.remove(3) #it will remove the first item from the list whose value is what you specified
print(datas)
datas.remove(4)
print(datas)
print("------------------------break-------------------------------")
#list method = index,count,sort,reverse and join
datass = [1,2,3,4,5,6,7,0,9,8,7,7,9,9,9,2]
datass.index(3) # returns the index of the specified item in the list
print(datass.index(3))
print(datass.index(9))
print(datass.count(7)) # returns how many times the item appears in the list
names = ['b', 'c', 'a', 'e', 'd']
names.reverse()
print(names)
namess = ['ba', 'cc', 'aa', 'ea', 'da']
namess.sort()
print(namess)
words = ['Coding', 'is', 'fun'] ## not installed (join)
print(words)

print("------------------------break start of exercise at the bottom-------------------------------")
# Create a list called instructors
instructors = []
# Add the following strings to the instructors list
# "Colt"
# "Blue"
# "Lisa"
instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")
# Remove the last value in the list
instructors.pop(-1)
# Remove the first value in the list
instructors.pop(0)
# Add the string "Done" to the beginning of the list
instructors.insert(0, 'Done')
# Run the tests to make sure you've done this correctly!
print(instructors)
