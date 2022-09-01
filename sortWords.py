def sort_words(input):
    return ' '.join(sorted(input.lower().split(), key = str.casefold))

print(sort_words("My name is Ahmad"))