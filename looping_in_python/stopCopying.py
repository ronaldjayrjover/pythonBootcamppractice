'''
ask for input
user gave response
prints out the same response
then if you say stop copying me the code breaks
'''

copy = input("what is going on: ")
while copy != "stop copying me":
    print(copy)
    copy = input("")

####yehey nagawa ko :D

##refactor from teacher

msg = input("say: ")
while msg != "stop":
    msg = input(f"{msg}\n")

