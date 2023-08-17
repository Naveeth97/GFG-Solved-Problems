#User function Template for python3

def rotate( arr, n):
    flag = arr[0]
    temp = 0
    for i in range(1,n):
        temp = flag
        flag = arr[i]
        arr[i] = temp
    arr[0] = flag
    return arr
        
        
        
        
        
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends