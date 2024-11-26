#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def find_maximum(value1,value2):
    
    if(value1>value2):
        return value1
    return value2
    
def find_minimum(value1,value2):
    if(value1<value2):
        return value1
    return value2

def normal_maximum(arr,n):
    maximum_ending = arr[0]
    maximum_sum = arr[0]
    
    for i in range(1,n):
        maximum_ending = find_maximum(maximum_ending + arr[i], arr[i])
        maximum_sum = find_maximum(maximum_ending,maximum_sum)
        
    return maximum_sum
    
def circular_minimum(arr,n):
    minimum_ending = arr[0]
    minimum_sum = arr[0]
    
    for i in range(1,n):
        minimum_ending = find_minimum(minimum_ending + arr[i], arr[i])
        minimum_sum = find_minimum(minimum_ending, minimum_sum)
        
        
    return minimum_sum
    
def circularSubarraySum(arr):
    ##Your code here
    #Time complexity: O(n)
    
    n = len(arr)
    
    total_array_sum = 0
    normal_maximum_sum = normal_maximum(arr,n)
    
    if(normal_maximum_sum<0):
        return normal_maximum_sum
        
    
    circular_maximum_sum = circular_minimum(arr,n)
    
    #total sum of an array
    for j in range(n):
        total_array_sum += arr[j]
        
    circular_maximum_sum = total_array_sum - circular_maximum_sum
    
    return find_maximum(circular_maximum_sum,normal_maximum_sum)





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends