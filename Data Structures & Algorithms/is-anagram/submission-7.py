class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = set(s)
        b = set(t)
        if (a != b or len(s) != len(t)):
            return False
        
        NrAparS = {}
        NrAparT = {}

        for i in range(len(s)):
            NrAparS[s[i]] = NrAparS.get(s[i], 0) + 1
            NrAparT[t[i]] = NrAparT.get(t[i], 0) + 1

        return NrAparS == NrAparT