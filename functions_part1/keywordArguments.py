#why use keyword arguments
### its more flexible on passing parameters

##it is diff from default params
## when you define a function and use an = , you are setting a default parameter
## when you invoke a function and use an = , you are making a keyword argument

def full_name(first="jay", last="jover"):
    return f"your name is {first} {last}"

print(full_name()) ### using default params your name is jay jover
print(full_name(last="enthusiast", first='python')) #### keyword argumenr your name is python enthusiast