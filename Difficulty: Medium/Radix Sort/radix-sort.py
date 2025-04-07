#User function Template for python3

def radixSort(arr, n):
    # code here
    
    max_element = get_max_element(arr, n)
    exp = 1
    
    while max_element // exp > 0:
        
        count_sort(arr, n, exp)
        exp *= 10
        
    
def count_sort(arr, n, exp):
    
    res = [0] * len(arr)
    count = [0] * 10
    
    for i in range(len(arr)):
        
        count[(arr[i] // exp) % 10] += 1
        
    for i in range(1, 10):
        
        count[i] += count[i - 1]
        
    for i in range(len(arr) - 1, -1, -1):
        
        res[count[(arr[i] // exp) % 10] - 1] = arr[i]
        count[(arr[i] // exp) % 10] -= 1
        
    for i in range(len(res)):
        
        arr[i] = res[i]
    
def get_max_element(arr, n):
    
    max_element = -(1 << 31)
    
    for i in arr:
        
        max_element = max(max_element, i)
        
    return max_element


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    while(t>0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        radixSort(arr, n)
        for ele in arr:
            print(ele, end=" ")
        print()
        t = t-1

        print("~")
# } Driver Code Ends