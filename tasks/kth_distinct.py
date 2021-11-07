# No. 2053

def kthDistinct(arr, k):
    c = Counter(arr)
    l = []
    
    for s in arr:
         if c[s] == 1:
            l.append(s)
            
    if len(l) < k:
        return ""
    else:
        return l[k-1]

arr = ["d","b","c","b","c","a"]
k = 2

print(arr, k)