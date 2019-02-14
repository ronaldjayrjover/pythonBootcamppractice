'''
print the following beautiful art using
both a for loop and a while loop
emoji = print("\U0001f600") 1 to 10 smiley faces
'''


for emojis in range(1, 11):
    print("\U0001f600" * emojis)

emoji = 1
while emoji < 11:
    print("\U0001f600" * emoji)
    emoji += 1

for x in range(3): ### nested loop; x is the external loop
    for emojis in range(1, 11):
        print("\U0001f600" * emojis)

for emojis in range(1, 11):  ### long way of writting, without a multiplication
    count = 1
    smileys = ""
    while count <= emojis:
        smileys += "\U0001f600"
        count += 1
    print(smileys)

