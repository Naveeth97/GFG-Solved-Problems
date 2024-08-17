#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        
        count_zero = 0
        product = 1
        
        for i in range(len(nums)):
            
            if nums[i] == 0:
                count_zero += 1
                continue
            
            product *= nums[i]
            
        
        if count_zero > 1:
            
            return [0] * len(nums)
        elif count_zero == 1:
            
            for i in range(len(nums)):
                
                if nums[i] == 0:
                    nums[i] = product 
                    
                else:
                    nums[i] = 0
        else:
            
            for i in range(len(nums)):
                
                nums[i] = product // nums[i]
                
        return nums
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends