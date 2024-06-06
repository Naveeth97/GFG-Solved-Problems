#User function Template for python3

def max_sum(a,n):
    #code here
    total_sum = 0
    for i in range(n):
        total_sum += a[i]
        
    current_value = 0
    
    for i in range(n):
        current_value += (i * a[i])
        
    max_sum = current_value
    
    for i in range(1, n):
        current_value = current_value + total_sum - n * a[n - i]
        max_sum = max(max_sum, current_value)
        
    return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends