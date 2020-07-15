class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        short = float("inf")
        ss = strs[0]
        for st in strs:
            if len(st) < short:
                short = len(st)
                ss = st
        print(short)
        for i in range(short):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return ss