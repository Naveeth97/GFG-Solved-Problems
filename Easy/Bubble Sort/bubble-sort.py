#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        if(n==0 or n == 1):
            return arr
            
        i = 0
        while(i<n):
            swap = False
            j = 1
            while(j<n-i):
                if(arr[j]<arr[j-1]):
                    temp = arr[j]
                    arr[j] = arr[j-1]
                    arr[j-1] = temp
                    swap = True
                j+=1
            if(swap == False):
                break
            i+=1
        return arr
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends