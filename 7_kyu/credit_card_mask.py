
def maskify(cc):
    a = cc[:-4]
    c = len(a)
    b = cc[-4:]

    return a.replace(a,'#' * c) + b

print(maskify('657489345'))