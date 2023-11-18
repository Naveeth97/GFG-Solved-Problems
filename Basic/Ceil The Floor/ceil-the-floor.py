#User function Template for python3




def getFloorAndCeil(arr, n, x):
    # code here
    floor,ceil = -1,-1
    floor_x = 2**32
    ceil_x = 2**32
    
    for i in range(n):
        
        if(arr[i]<=x and x - arr[i]<floor_x):
            floor = arr[i]
            floor_x = x - arr[i]
            
        if(arr[i]>=x and arr[i] - x < ceil_x):
            ceil = arr[i]
            ceil_x = arr[i] - x
            
    return [floor,ceil]
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = getFloorAndCeil(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends