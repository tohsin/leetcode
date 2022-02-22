class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dfs(i,state):
            if i>=len(prices):
                return 0
            
            cooldown = dfs(i+1,state)
            if state=='buy':
                '''
                if current  state is sell you want to either buy now or cool down
                to buy you loose money and skip to next one and change the state
                '''
                buy = dfs(i+1,'sell')-prices[i]
                return max(buy, cooldown)

            else:
            
                '''
                either sell or take a cool down
                sell means you add to profit and have to skip two days
                cool doown means you have to skip days not gain or lose profit
                but state to buy remains the same
                '''
                #either sell or take a cool down
                #sell means changing state and moving index and increasing total profit but you have too cool down
                #
                sell = dfs(i+2,'buy')+prices[i]
                
                return max(sell, cooldown)
           
        return dfs(0,'buy')