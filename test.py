def checkInclusion(s1, s2):
    i = 0
    l = len(s1)
    
    subs = []
    
    
    for j in range(l, len(s2)):
        # if sorted(s1) == sorted(s2[i:j]):
        #     return True
        # j += l
        subs.append(s2[i:j])
        i += 1
    return subs

s1 = "ab"
s2 = "eidbaooo"

print(checkInclusion(s1, s2))