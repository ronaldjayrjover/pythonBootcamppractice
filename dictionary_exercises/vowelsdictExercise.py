#create a dictionary with the key as vowel in the alphabet and the value as 0.
#Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
#do this programmatically (using dict comprehension or dict method) rather than hard coding

# make sure your solution is assigned to the answer variable so the tests can work!
vowel = ["a", "e", "i", "o", "u"]
answer = {}.fromkeys(vowel, 0) #from dict.fromkeys()
answer2 = {char:0 for char in 'aeiou'}
print(answer, answer2)