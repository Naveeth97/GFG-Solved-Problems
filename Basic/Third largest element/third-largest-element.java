//{ Driver Code Starts
import java.util.Scanner;
import java.util.*;
import java.io.*;

class ThirdLargestElement
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t>0)
		{
			int n =sc.nextInt();
			int arr[] = new int[n];
			for(int i=0;i<n;i++)
				arr[i] = sc.nextInt();
			Solution g = new Solution();
			System.out.println(g.thirdLargest(arr,n));
		t--;
		}
	}
}
// } Driver Code Ends


class Solution
{
    int thirdLargest(int a[], int n)
    {
	    // Your code here
	    int largest = 0,secondLargest = 0,thirdLargest = 0;
	    
	    if(n<3){
	        return -1;
	    }
	    for(int i = 0;i<n;i++){
	        if(a[i]>largest){
	            thirdLargest = secondLargest;
	            secondLargest = largest;
	            largest = a[i];
	        }
	        else if(a[i]>secondLargest && a[i] != secondLargest){
	            thirdLargest = secondLargest;
	            secondLargest = a[i];
	        }
	        else if(a[i]>thirdLargest && (a[i] != secondLargest && a[i] != largest)){
	            thirdLargest = a[i];
	        }
	    }
	    
	    if(thirdLargest == 0){
	        return -1;
	    }
	    return thirdLargest;
	                                        
    }
}
