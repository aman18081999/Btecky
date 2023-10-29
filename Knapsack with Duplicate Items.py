class Solution:
    def knapSack(self, N, W, val, wt):
        
        n = N
        dp = [[0] * (W+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,W+1):
                
                if wt[i-1] <= j:
                    dp[i][j] = max(dp[i-1][j], val[i-1] + dp[i][j - wt[i-1]])
                    
                else: 
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][W]
