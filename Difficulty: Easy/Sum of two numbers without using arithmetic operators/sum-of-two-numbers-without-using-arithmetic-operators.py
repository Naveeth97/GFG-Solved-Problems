#User function Template for python3

def sum(a,b):
    #code here
    
    sum = 0
    pow = 1
    
    while a != 0 or b != 0:
        
        if a & 1 == 1:
            
            sum += pow
            
        if b & 1 == 1:
            
            sum += pow
            
        a >>= 1
        b >>= 1
        pow <<= 1
        
    return sum
            
            


#{ 
 # Driver Code Starts
import math
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        inp = list(map(int,input().split())) 
        
        a=inp[0]
        b=inp[1]
        
        #ob=Solution()
        print(sum(a,b))
     
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends