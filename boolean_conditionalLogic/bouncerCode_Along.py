##ask for age
##18021 wristband
##21+ drink, normal entru
##too young, sorry

age = input("What is your age: ")

if age: ### this is true even if its a string or integer but if its empty string it will go to a break
    age = int(age)
    if age >= 18 and age <= 21:
        print("So you can enter, but need a wristband")
    elif age >= 21:
        print("You can enter normally")
    else:
        print("You cant enter")
else:
    print("Plese enter a number")