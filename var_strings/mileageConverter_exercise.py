print("How many km did you run today")
kms = input()
mi = float(kms)/1.60934
mi = round(mi, 2)
print("Ok you said {}".format(mi))
print("or")
print(f"Ok you said {mi}")
print("Your {}km ride is {}mi".format(kms, mi))
print("or")
print(f"Your {kms}km ride is {mi}mi") ###python 3 f string