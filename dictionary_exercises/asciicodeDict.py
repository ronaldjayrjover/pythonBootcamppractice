#chr forr 64 to 90 and output is 65: A, 66: B ......

#Use chr() on the numbers between 65 and 91:
answer = {count: chr(count) for count in range(65,91)}
print(answer)