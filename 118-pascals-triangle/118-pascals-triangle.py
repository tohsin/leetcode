class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        ans=[[1],[1,1]]
        if numRows<3:
            return ans[:numRows]
        for i in range(numRows-2):
            curr=ans[-1] #121
            cache=[1]   
            
            for j in range(1,len(curr)):  #3.   1,2 
                cache.append(curr[j]+curr[j-1])
            cache.append(1)
                
            ans.append(cache)
        return ans
            
        