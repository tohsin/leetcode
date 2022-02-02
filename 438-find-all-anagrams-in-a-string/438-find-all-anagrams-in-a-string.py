class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        s_len = len(s)
        
        if (p_len > s_len): return []
        
        def isanagram(bag,cache)->bool:
            if len(bag)!=len(cache):
                return False
            count=0
            for key in bag:
                if key not in cache: # guy isnt included there so return val
                    return False
                if bag[key]!=cache[key]:
                    return False
                count+=1
            if count!=len(cache):
                return False
            return True
        cache = {}
        ans=[]
        for i in range(len(p)):
            if p[i] in cache:
                cache[p[i]]+=1
            else:
                cache[p[i]]=1
        #sliding window
        bag = {}
        k = len(p)
        for i in range(k):
            if s[i] in bag:
                bag[s[i]] += 1
            else:
                bag[s[i]] = 1
        if isanagram(bag, cache):
            ans.append(i-k+1)
        for j in range(k,len(s)): #k=3 j=3 e // remove c
            if s[j] in bag:
                bag[s[j]]+=1
            else:
                bag[s[j]]=1
            if bag[s[j-k]]-1==0:
                del bag[s[j-k]]
            else:
                bag[s[j-k]]-=1
            if isanagram(bag,cache):
                ans.append(j-k+1)
        return ans