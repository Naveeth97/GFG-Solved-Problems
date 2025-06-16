class Solution:
    def minCost(self, heights, cost):
        # code here
        
        ans = float('inf')
        
        low = (1 << 31)
        high = -(1 << 31)
        
        for i in range(len(cost)):
            
            low = min(low, heights[i])
            high = max(high, heights[i])
            
        while low < high:
            
            mid = low + (high - low) // 2
            
            cost1 = self.find_cost(cost, heights, mid)
            cost2 = self.find_cost(cost, heights, mid + 1)
            
            if cost1 <= cost2:
                
                high = mid
            else:
                
                low = mid + 1
                
        return self.find_cost(cost, heights, low)
        
    def find_cost(self, cost, height, mid):
        
        total_cost = 0
        
        for i in range(len(height)):
            
            total_cost += abs(height[i] - mid) * cost[i] 
            
        return total_cost
        
        