def display_names(first, second):
    print(f"{first} hello {second}")
names = {"first": "jay", "second": "ron"}
display_names(**names)

def add_and_multiply_numbers(a,b,c, **kwargs):
    print(a + b * c)
    print("anything")
    print(kwargs)
data = dict(a=1, b=2, c=2, m=100, name="jayjay")
add_and_multiply_numbers(**data)