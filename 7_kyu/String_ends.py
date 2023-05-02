def solution(text, ending):
    n = len(ending)
    if text[-n:] == ending:
        return True
    else:
        return False

# Решение через endwith
# def solution(string, ending):
#     if string.endswith(ending):
#     	return True
#     return False