class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uniqueSet_S = {}
        uniqueSet_T = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            uniqueSet_S[s[i]] = 1 + uniqueSet_S.get(s[i],0)
            uniqueSet_T[t[i]] = 1 + uniqueSet_T.get(t[i],0)

        for key, val in uniqueSet_S.items():
            if val != uniqueSet_T.get(key):
                return False
        return True

        