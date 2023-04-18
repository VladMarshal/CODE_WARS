def binary_array_to_number(arr):
        dlina = len(arr)
        chislo_dec = 0
        for i in range(0, dlina):
            chislo_dec = chislo_dec +int(arr[i]) * (2**(dlina-i-1))
        return chislo_dec

print(binary_array_to_number([1,1,1,1]))