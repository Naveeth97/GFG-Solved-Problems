//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
class GfG
{
    public static void main (String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            
            String a = sc.next();
            String b = sc.next();
            Solution ob = new Solution();
            if(ob.isSubSequence(a,b))
            System.out.println(1);
            else
            System.out.println(0);
 		
        }
    }
}


// } Driver Code Ends


//User function Template for Java

class Solution{
    boolean isSubSequence(String A, String B){
        
        if(A.length() > B.length()){
            return false;
        }
        
        int i = 0, j = 0;
        
        
        while(i<B.length() && j < A.length()){
            
            if(B.charAt(i) == A.charAt(j)){
                j += 1;
            }
            i += 1;
        }
        
        if(j == A.length()){
            return true;
            
        }
        return false;
    }
}