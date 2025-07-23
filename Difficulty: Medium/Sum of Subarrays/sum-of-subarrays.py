class Solution:
    def subarraySum(self, arr):
        # code here 
        
        sum = 0
        n = len(arr)
        
        for i in range(n):
            
            sum += arr[i] * (i + 1) * (n - i)
            
        return sum
        