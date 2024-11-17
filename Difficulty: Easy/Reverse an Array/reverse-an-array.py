class Solution:
    def reverseArray(self, arr):
        # code here
        
        start = 0
        end = len(arr) - 1
        
        while start < end:
            
            self.swap(start, end, arr)
            start += 1
            end -= 1
            
        
            
    def swap(self, start, end, arr):
        
        arr[start] ^= arr[end]
        arr[end] ^= arr[start]
        arr[start] ^= arr[end]
        
        
        
        
        


#{ 
 # Driver Code Starts
import sys


def main():
    # Read the number of test cases
    tc = int(sys.stdin.readline())

    while tc > 0:
        # Read the array elements as a string
        str_arr = sys.stdin.readline().split()

        # Convert the string array to an integer array
        arr = [int(x) for x in str_arr]

        # Create a Solution object
        obj = Solution()

        # Reverse the array
        obj.reverseArray(arr)

        # Print the reversed array
        for i in range(0, len(arr)):
            print(arr[i], end=" ")
        print()
        print("~")

        # Decrement the test case count
        tc -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends