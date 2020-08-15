def levenshteinDistance(str1, str2):
    smaller = str1 if len(str1) < len(str2) else str2
    bigger = str1 if len(str1) >= len(str2) else str2
    evens = [x for x in range(len(smaller) + 1)]
    odds = [None for x in range(len(smaller) + 1)]
    for i in range(1, len(bigger) + 1):
        if i % 2 == 0:
            current = evens
            previous = odds
        else:
            current = odds
            previous = evens
        current[0] = i
        for j in range(1, len(smaller) + 1):
            if bigger[i - 1] == smaller[j - 1]:
                current[j] = previous[j - 1]
            else:
                current[j] = 1 + min(current[j - 1], previous[j - 1], previous[j])
    return evens[-1] if len(bigger) % 2 == 0 else odds[-1]