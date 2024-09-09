class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        low, high = 0, len(arr) - 1
        
        mid = 0
        
        while mid <= high:
            
            temp = arr[mid]
            
            if (arr[mid] == 0):
                arr[mid] = arr[low]
                arr[low] = temp
                mid += 1
                low += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid] = arr[high]
                arr[high] = temp
                high -= 1
                
        return arr
                
                
            
        
        


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array


if __name__ == "__main__":
    main()

# } Driver Code Ends