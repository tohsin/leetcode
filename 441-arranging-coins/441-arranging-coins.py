class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        n_steps = 1
        while True:
            if n_steps<=n:
                #can fit
                n-=n_steps
                n_steps+=1
                count+=1
            else:
                break
        return count