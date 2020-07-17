class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = {}
        for email in emails:
            parts = email.split("@")
            newStr = parts[0].replace(".", "").split("+")[0]
            if parts[1] not in d:
                d[parts[1]] = set()
            d[parts[1]].add(newStr)
        count = 0
        for i in d:
            count += len(d[i])
        return count