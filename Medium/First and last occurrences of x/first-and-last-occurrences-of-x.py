#User function Template for python3
def firstoccurence(arr,n,x):
    if(n == 0):
        return 0
    start,end = 0,n-1
    while(start<=end):
        mid = (start + end)//2
        if(arr[mid]>x):
            end = mid - 1
        elif(arr[mid]<x):
            start = mid + 1
        else:
            if(mid == 0 or arr[mid] == x and arr[mid-1] != x):
                return mid
            else:
                end = mid - 1
            
def lastoccurence(arr,n,x):
    if(n == 0):
        return 0
    start,end = 0, n-1
    while(start<=end):
        mid = (start + end)//2
        if(arr[mid]>x):
            end = mid -1
        elif(arr[mid]<x):
            start = mid + 1
        else:
            if(mid == n - 1 or arr[mid] == x and arr[mid+1] != x):
                return mid
            else:
                start = mid + 1


def find(arr,n,x):
    # code here
    
    i = firstoccurence(arr,n,x)
    j = lastoccurence(arr,n,x)
    
    if(i == None or j == None):
        return -1,-1
    return i,j
    
    
    

    



#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends