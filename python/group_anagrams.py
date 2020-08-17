def groupAnagrams(words):
    s = {}
    for word in words:
        sWord = "".join(sorted(word))
        if sWord not in s:
            s[sWord] = []
        s[sWord].append(word)
    return list(s.values())