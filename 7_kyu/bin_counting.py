def square_digits(num):
    a = ''
    num = str(num)
    for i in num:
        a += str(int(i) ** 2)
    return int(a)

print(square_digits(1018))