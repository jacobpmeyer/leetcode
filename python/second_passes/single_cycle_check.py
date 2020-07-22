def hasSingleCycle(array):
    count = 0
    i = 0
    while True:
        i += array[i]
        count += 1
        if i < 0 or i >= len(array):
            i %= len(array)
        if count >= len(array) or i == 0:
            if count >= len(array) and i == 0:
                return True
            else:
                return False