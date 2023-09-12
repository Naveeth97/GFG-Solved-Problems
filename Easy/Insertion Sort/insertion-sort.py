#Sort the array using insertion sort

class Solution:
    def insert(self, alist, index, n):
        #code here
        arr = []
        for i in range(n):
            arr.append(i)
        return arr
            
        
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        for j in range(0,n-1):
            k = j + 1
            while(k>0):
                if(alist[k]<alist[k-1]):
                    temp =alist[k]
                    alist[k] = alist[k-1]
                    alist[k-1] = temp
                else:
                    break
                k-=1
        return alist


#{ 
 # Driver Code Starts

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends