import collections
def duplicate_count(text):
    check = 0
    new_text = text.lower()
    counter = collections.Counter(new_text)
    for i in list(counter.values()):
        if i > 1:
            check += 1
    return check
print(duplicate_count('Indivisibilities'))