#User function Template for python3
class Solution:
    
    def rotateMatrix(self,arr, n):
        # code here
        
        for i in range(len(arr)):
            
            self.reverse(arr, i)
            
        for i in range(len(arr)):
            
            for j in range(i + 1, len(arr[0])):
                
                self.swap(i, j, arr)
                
        
    
    def reverse(self, arr, row):
        
        i = 0
        j = len(arr[row]) - 1
        while(i <= j):
            
            temp = arr[row][j]
            arr[row][j] = arr[row][i]
            arr[row][i] = temp
            i+=1
            j-=1
            
    def swap(self, fir, lst, arr):
        
        temp = arr[fir][lst]
        arr[fir][lst] = arr[lst][fir]
        arr[lst][fir] = temp
            
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                arr[i][j] = inputLine[i * n + j]
        ob = Solution()
        ob.rotateMatrix(arr, n)
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=" ")
        print()
        tc -= 1

# } Driver Code Ends