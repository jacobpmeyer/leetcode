def addBinary(a, b):
    if a == "0" and b == "0":
        return "0"
    p = count = 0
    res = []
    for i in range(len(a)):
        j = len(a) - i - 1
        count += int(a[j]) * 2**p
        p += 1
    p = 0
    for i in range(len(b)):
        j = len(b) - i - 1
        count += int(b[j]) * 2**p
        p += 1
    while count > 1:
        s = str(count % 2)
        count //= 2
        res.append(s)
    res.append("1")
    return "".join(reversed(res))


a = ("100")
b = ("1")

print(addBinary(a, b))