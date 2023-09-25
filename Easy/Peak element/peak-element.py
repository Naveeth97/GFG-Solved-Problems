# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        if(n==0 or n ==1):
            return 0
        elif(arr[0]>=arr[1]):
            return 0
        elif(arr[n-1]>=arr[n-2]):
            return n-1
        
            
        start,end = 0,n-1
        while(start<=end):
            mid = (start + end)//2
            if(arr[mid]>=arr[mid+1] and arr[mid]>=arr[mid-1]):
                return mid
            elif(arr[mid-1]>arr[mid]):
                end = mid - 1
            else:
                start = mid + 1
                
            



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends