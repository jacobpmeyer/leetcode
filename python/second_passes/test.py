def checker(obj, arr):
    for i in arr:
        if i in obj:
            print(True)
        else:
            print(False)
    return "DONE"

obj = {1: "a", "b": 2}
arr = [1, 2]
print(checker(obj, arr))