class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        
        if len(s) != len(pattern):
            return False
        
        d = {}
        e = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = pattern[i]
            else:
                if d[s[i]] != pattern[i]:
                    return False
                
            if pattern[i] not in e:
                e[pattern[i]] = s[i]
            else:
                if e[pattern[i]] != s[i]:
                    return False
        return True
        