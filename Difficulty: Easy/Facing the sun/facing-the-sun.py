#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        sun_max = -(1 << 31)
        count = 0
        
        for i in height:
            
            if i > sun_max:
                count += 1
            sun_max = max(sun_max, i)
            
        return count
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        height = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(height)
        print(ans)

# } Driver Code Ends