#purple should be in the argument, True if its there and false other wise

def contains_purple(*color):
    if "purple" in color:
        return True
    return False

print(contains_purple('red', '1'))
print(contains_purple('purple', '1'))
