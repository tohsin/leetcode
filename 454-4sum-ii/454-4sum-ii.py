class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cache = {}
        ans=0
        for num1 in nums1:
            for num2 in nums2:
                v= num1+num2
                if v in cache:
                    cache[v]+=1
                else:
                    cache[v] = 1
        print(cache)
        for num3 in nums3:
            for num4 in nums4:
                v= num3+num4
                v= -1*v
                if v in cache:
                    ans+=1*cache[v]
        print(ans)
        return ans
        
        
            