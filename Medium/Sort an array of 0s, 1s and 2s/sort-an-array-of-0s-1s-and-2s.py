class Solution:
    def sort012(self,arr,n):
        # code here
        #Dutch National Flag Algorithm
        low,mid,high = 0,0,len(arr) - 1
        while(mid<=high):
            if(arr[mid] == 0):
                flag = arr[low]
                arr[low] = arr[mid]
                arr[mid] = flag
                low += 1
                mid += 1
            elif(arr[mid] == 1):
                mid += 1
            else:
                flag = arr[high]
                arr[high] = arr[mid]
                arr[mid] = flag
                high -= 1
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends