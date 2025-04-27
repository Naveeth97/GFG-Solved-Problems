//{ Driver Code Starts
// Initial Template for Java

import java.math.*;
import java.util.*;

class Multiply {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            String a = sc.next();
            String b = sc.next();
            Solution g = new Solution();
            System.out.println(g.multiplyStrings(a, b));

            System.out.println("~");
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    public String multiplyStrings(String s1, String s2) {
        // code here.
        
        int s1Len = s1.length() - 1;
        int s2Len = s2.length() - 1;
        
        int sign = 1;
        
        if (s1.charAt(0) == '-' || s2.charAt(0) == '-') {
            
            if (s1.charAt(0) == '-') {
                sign = -1;
            }
            
            if (s2.charAt(0) == '-') {
                sign *= -1;
            }
        }
        
        // we want to store the result in an array of whole multiplication
        // using manual method of multiplication
        
        int[] result = new int[s1Len + s2Len + 2];
        
        int i1 = 0;
        int i2 = 0;
        
        while (s1Len >= 0) {
            
            if (s1.charAt(s1Len) == '-') break;
            
            
            int num1 = s1.charAt(s1Len) - '0';
            int carry = 0;
            int temp = s2Len;
            i2 = 0;
            
            while (temp >= 0) {
                
                if (s2.charAt(temp) == '-') break;
                
                int num2 = s2.charAt(temp) - '0';
                
                int sum = num1 * num2 + result[i1 + i2] + carry;
                
                carry = sum / 10;
                result[i1 + i2] = sum % 10;
                i2++;
                temp--;
                
            }
            
            if (carry > 0) {
                result[i1 + i2] += carry;
            }
            
            i1++;
            s1Len--;
        }
        
        String finalAns = "";
        
        int index = result.length - 1;
        
        while (index >= 0 && result[index] == 0) {
            
            index--;
        }
        
        while (index >= 0) {
            finalAns += Integer.toString(result[index--]) ;
        }
        
        if (finalAns.length() == 0) return "0";
        
        // System.out.println(sign);
        
        return (sign == -1) ? '-' + finalAns : finalAns;
        
    }
}