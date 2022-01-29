class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num)<3:
            return False
        def back(nums,ans,indx):
            if indx==len(nums):
                if(len(ans)>2):
                    if (ans[len(ans)-1]== (ans[len(ans)-2]+ ans[len(ans)-3])):
                        return True
            if len(ans)>2 and ans[len(ans)-1]!= (ans[len(ans)-2]+ ans[len(ans)-3]):
                return False
            for k in range(indx,len(nums)):
                    curr=nums[indx:k+1]
                    if len(curr)>1 and curr[0]=="0":
                        return
                    curr=int(curr)
                    # if len(str(curr))>3:
                    #     return
                    if len(ans)>2 and ans[len(ans)-1]>(ans[len(ans)-2]+ ans[len(ans)-3]):
                        return
                    ans.append(curr)
                    if back(nums,ans,k+1):
                        return True
                    else:
                        
                        ans.pop(len(ans)-1)
                    
        return back(num,[],0)