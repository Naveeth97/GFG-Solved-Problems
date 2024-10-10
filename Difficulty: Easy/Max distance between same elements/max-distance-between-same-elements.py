class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        
        max_distance = 0
        
        maps = {}
        
        for i in range(len(arr)):
            
            if arr[i] in maps:
                max_distance = max(max_distance, i -  maps[arr[i]])
            else:
                maps[arr[i]] = i
            
        return max_distance

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends