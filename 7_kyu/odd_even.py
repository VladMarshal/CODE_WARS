def odd_or_even(arr):
    a = 0
    for i in arr:
        a += i
    if a % 2 == 0:
        return 'even'
    else:
        return 'odd'


print(odd_or_even([0, 1, 2]))