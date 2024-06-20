def minCostClimbingStairs(cost):
    n=len(cost)
    if n==0:
        return 0
    elif n==1:
        return cost[0]
    
    #Initialize dp array to store the minimum cost to reach each step
    dp = [0]*n
    dp[0]=cost[0]
    dp[1]=cost[1]

     # Fill the dp array
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    # The answer will be the minimum cost to reach either of the last two steps
    return min(dp[n-1], dp[n-2])

# Example usage:
cost1 = [10, 12, 20]
cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost1))  # Output: 12
print(minCostClimbingStairs(cost2))  # Output: 6
    