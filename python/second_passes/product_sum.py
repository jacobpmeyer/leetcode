# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth = 1):
    if not len(array):
        return 0
    total = 0
    for el in array:
        if type(el) is list:
            total += productSum(el, depth + 1)
        else:
            total += el
    return total * depth