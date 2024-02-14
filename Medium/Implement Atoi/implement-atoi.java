//{ Driver Code Starts
//Initial template for JAVA

import java.util.Scanner;

class aToi
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		sc.nextLine();
		while(t>0)
		{
			String str = sc.nextLine();
			
			Solution obj = new Solution();
			int num = obj.atoi(str);
			
			System.out.println(num);
		t--;
		}
	}
}
// } Driver Code Ends


//User function template for JAVA

/*You are required to complete this method */
class Solution
{
    int atoi(String s) {
	// Your code here
	
	double value = 0;
	
// 	int sign = 1;
	
	if(s.length() == 0){
	    return -1;
	}
	
	if(s.charAt(0) == ' ' && s.charAt(s.length() - 1) == ' '){
	    return -1;
	}
	
	int i = 0, sign = 1;
	
	if(s.charAt(0) == '-'){
	    sign = -1;
	    i++;
	}
	
	while(i<s.length() && s.charAt(i) >= '0' && s.charAt(i) <= '9'){
	    
	    value = value * 10 + s.charAt(i) - '0';
	    
	    i++;
	}
	
	if(i != s.length()){
	    return -1;
	}
	
	value = sign * value;
	
	
	return (int)value;
	
	
	
	
    }
}
