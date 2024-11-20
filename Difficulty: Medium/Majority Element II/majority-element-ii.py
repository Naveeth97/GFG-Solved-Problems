class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        
        maps = {}
        
        result = []
        
        for i in range(len(arr)):
            
            if arr[i] in maps:
                maps[arr[i]] += 1
            else:
                maps[arr[i]] = 1
                
        size = len(arr) // 3
        
        for i in maps:
            
            if maps[i] > size:
                result.append(i)
                
        if len(result) == 0:
            
            return []
            
        return sorted(result)

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
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends