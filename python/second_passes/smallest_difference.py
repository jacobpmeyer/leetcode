# O(n*log(n) + m*log(m)) Time | O(1) Space
# where n is the length of arrayOne and m is the length of arrayTwo
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    left = 0
    right = 0
    current = float("inf")
    smallest = float("inf")
    smallestPair = []
    while left < len(arrayOne) and right < len(arrayTwo):
        firstNum, secondNum = arrayOne[left], arrayTwo[right]
        if firstNum < secondNum:
            current = secondNum - firstNum
            left += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            right += 1
        else:
            return [firstNum, secondNum]
        if current < smallest:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair