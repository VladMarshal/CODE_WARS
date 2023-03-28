def past(h, m, s):
    # 1 seconds = 1000 milliseconds
    # 1 minute = 60000 milliseconds
    # 1 hour = 3600000 milliseconds
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        s = s * 1000
        m = m * 60000
        h = h * 3600000
        result = s + m + h
        return result
    else:
        return None


print(past(1, 1, 1))