#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        # code herr
        if(k>Arr[N-1]):
            return N
        if(k<Arr[0]):
            return 0
        
        start,end = 0,N-1
        while(start<=end):
            mid = (start + end )//2
            
            if(Arr[mid]== k):
                return mid
            elif(Arr[mid]>k):
                end = mid - 1
            else:
                start = mid + 1
        return end + 1
        
            
                    
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends