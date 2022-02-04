class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cache = {}
        cache[0] = -1
        max_len = 0
        count = 0
        for i in range(len(nums)):
            v = 1 if nums[i]==1 else -1
            count += v
            if  count in cache:
                max_len=max(max_len,i-cache[count])
            else:
                cache[count] = i
        return max_len