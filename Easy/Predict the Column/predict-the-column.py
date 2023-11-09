#User function Template for python3

class Solution:
    def columnWithMaxZeros(self,arr,N):
        # code here 
        
        zeros_count = 0
        res = -1
        max = 0
        for i in range(N):
            zeros_count = 0
            
            for j in range(0,N):
                
                if(arr[j][i] == 0):
                    zeros_count +=1
                
            if(zeros_count>max):
                max = zeros_count
                res = i
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = []
        for i in range(N):
            line = [int(x) for x in input().strip().split()]
            arr.append(line)
        ob=Solution()
        print(ob.columnWithMaxZeros(arr,N))


# } Driver Code Ends