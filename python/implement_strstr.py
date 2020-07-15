# h is the length of the haystack, n is the length of the needle
# O((h - n)n) Time | O(1) Space
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, h = len(needle), len(haystack)
        if n == 0:
            return 0
        ph = 0
        while ph < h - n + 1:
            while ph < h - n + 1 and haystack[ph] != needle[0]:
                ph += 1
            pn = 0
            currLen = 0
            while ph < h and pn < n and haystack[ph] == needle[pn]:
                pn += 1
                currLen += 1
                ph += 1
            if currLen == n:
                return ph - currLen
            ph = ph - currLen + 1
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        if L > n:
            return -1
        
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2**31
        
        # lambda-function to convert character to integer
        h_to_int = lambda i : ord(haystack[i]) - ord('a')
        needle_to_int = lambda i : ord(needle[i]) - ord('a')
        
        # compute the hash of strings haystack[:L], needle[:L]
        h = ref_h = 0
        for i in range(L):
            h = (h * a + h_to_int(i)) % modulus
            ref_h = (ref_h * a + needle_to_int(i)) % modulus
            print(h)
            print(ref_h)
        if h == ref_h:
            return 0
        print("==========")
        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus) 
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
            print(h)
            if h == ref_h:
                return start

        return -1

needle = "cat"
haystack = "tacocat"
s = Solution()
print(s.strStr(haystack, needle))


12846 * 26 - 19 * pow(26, 3, 2**31) + 14 % 2**31

(12846 * 26) - 19 * pow(26, 3, 2**31) + 14 % 2**31