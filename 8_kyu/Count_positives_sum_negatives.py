def count_positives_sum_negatives(arr):
    positive_vailable = 0 # it's  for positive vailable
    negative_vailable = 0
    if len(arr) > 0:
        for i in arr:
            if i > 0:
                positive_vailable += 1
            elif i < 0:
                negative_vailable += i
        return [positive_vailable, negative_vailable]
    else:
        return []

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))