#User function Template for python3
class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        
        maps = { 0 : 1}
        
        count_x, count_y = 0, 0
        ans = 0
        
        for i in range(len(arr)):
            
            if arr[i] == x:
                count_x += 1
            
            if arr[i] == y:
                count_y += 1
                
            if count_x - count_y in maps:
                ans += maps[count_x - count_y]
                maps[count_x - count_y] += 1
            else:
                maps[count_x - count_y] = 1
                
        return ans
            
            
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        y = int(input().strip())
        ob = Solution()
        ans = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends