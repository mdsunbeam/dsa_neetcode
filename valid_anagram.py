#from typing import str

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        if s == t:
            return True
        return False

res = Solution()
print(res.isAnagram("anagram", "nagaram"))