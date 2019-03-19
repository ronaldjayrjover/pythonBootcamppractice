#combine_words("child")
#combine_words("child", suffix="ren")
#combine_words("child", suffix="man")


# Define combine_words below:
def combine_words(word, **kwargs):
        if 'prefix' in kwargs:
            return f"{kwargs['prefix']}" + f"{word}"
        elif 'suffix' in kwargs:
            return f"{word}" + f"{kwargs['suffix']}"

print(combine_words("child"))
print(combine_words("child", suffix="ren"))
print(combine_words("child", prefix="man"))
