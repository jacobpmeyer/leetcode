def longestPalindromicSubstring(string):
    i = 0
    long = string[0]
    while i < len(string) - 1:
        left = i - 1
        right = i + 1
        if left >= 0 and right < len(string) and string[i] == string[right] \
                and string[left] != string[right]:
            right += 1
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        if len(string[left + 1:right]) > len(long):
            long = string[left + 1:right]
        i = right
    return long
        
def longestPalindromicSubstring(string):
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        even = getLongestPalindromeFrom(string, i - 1, i)
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
    return string[currentLongest[0] : currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx]