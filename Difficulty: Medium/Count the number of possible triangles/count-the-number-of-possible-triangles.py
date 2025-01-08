#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        
        # to avoid the repeatation and time
        arr.sort()
        
        # to store the result of the how many traiangle
        count = 0
        
        for i in range(len(arr) - 1, -1, -1):
            
            left, right = 0, i - 1
            
            while left < right:
                
                if arr[left] + arr[right] > arr[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
                    
        return count
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends