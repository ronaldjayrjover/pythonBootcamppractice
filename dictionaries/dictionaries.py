#limittations of lists

cat = {"name": "blue", "age": 3.5, "isCute": True}  ## this is more used
print(cat)
print(cat["name"])

cat2 = dict(name2="kitty", age=0.5)
print(cat2["name2"])


'''
Exercise on accessing the dictionary
'''


artist = {
    "first": "Neil",
    "last": "Young",
}
full_name = artist["first"] + " " + artist["last"]
print(full_name)

print("#############break######")

instructor = {
    "name": "jay",
    "age": 36,
    "state": "quezon",
    "color": "blue"
}
###longway
print(instructor["name"])
print(instructor["age"])
####shortway
print("#####break using values on looping#####")
for value in instructor.values():
    print(value)
print("#####break   using keys on looping#####")
for keys in instructor.keys():
    print(keys)
print("#####break   using items  on looping and giving 2 items#####")
for keyss,valuess in instructor.items():
    print(f"key is {keyss} and value is {valuess}")

print("##########break#######")

# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!

# Use a loop to add together all the donations and store the resulting number in a variable called total_donations

total_donations = 0

for donation in donations.values():
    total_donations += donation
    print(total_donations)
#############
print("#####testing if there is an exisiting keys eg name or address")
print("name" in instructor)
print("address" in instructor)

print("#####testing if there is an exisiting values eg jay quezon")
print("jay" in instructor.values())
print("quezon" in instructor.values())
print("name" in instructor.values())



