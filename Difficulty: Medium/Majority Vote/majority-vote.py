class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        #Your Code goes here.
        result = []
        
        maps = {}
        
        for i in range(len(nums)):
            
            if nums[i] in maps:
                maps[nums[i]] += 1
            else:
                maps[nums[i]] = 1
                
        size = len(nums) // 3
        
        for i in maps:
            
            if maps[i] > size:
                result.append(i)
                
        if len(result) == 0:
            return [-1]
            
        sorted(result)
            
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends