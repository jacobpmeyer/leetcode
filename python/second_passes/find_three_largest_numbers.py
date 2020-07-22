def findThreeLargestNumbers(array):
    largest = [float("-inf") for x in range(3)]
    for num in array:
        for i in reversed(range(3)):
            if num > largest[i]:
                j = 0
                while j < i:
                    largest[j] = largest[j + 1]
                    j += 1
                largest[i] = num
                break
    return largest