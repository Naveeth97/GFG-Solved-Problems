//{ Driver Code Starts
// Initial Template for Java

// Initial Template for Java

import java.io.*;
import java.util.*;

public class validip {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            String s = sc.next();
            Solution obj = new Solution();

            if (obj.isValid(s))
                System.out.println("true");
            else
                System.out.println("false");

            System.out.println("~");
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {

    public boolean isValid(String s) {
        // Write your code here
        
        String[] str = s.split("[\\.]");
        
        if (str.length != 4) {
            return false;
        }
        
        for (String str1 : str) {
            
            if (str1.length() > 1 && str1.charAt(0) == '0') return false;
            
            if (str1.equals("")) return false;
            
            if (Integer.parseInt(str1) > 255 || Integer.parseInt(str1) < 0) {
                return false;
            }
            
            
        }
        
        return true;
    }
}