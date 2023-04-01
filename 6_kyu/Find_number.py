def find_it(seq):
    for i in seq:
        check_out = seq.count(i)
        if check_out % 2 == 0:
            continue
        else:
            return i


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))

