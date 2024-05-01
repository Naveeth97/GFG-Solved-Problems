//{ Driver Code Starts
/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;

class Node {
    char data;
    Node next;
    
    public Node(char data){
        this.data = data;
        next = null;
    }
}

class GFG {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-- > 0){
		    int n = sc.nextInt();
		    Node head = null, tail = null;
		    
		    char head_c = sc.next().charAt(0);
		    head = new Node(head_c);
		    tail = head;
		    
		    while(n-- > 1){
		        tail.next = new Node(sc.next().charAt(0));
		        tail = tail.next;
		    }
		    
		    Solution obj = new Solution();
		    //show(head);
		    show(obj.arrangeCV(head));
		    
		}
	}
	
	public static void po(Object o){
	    System.out.println(o);
	}
	
	public static void show(Node head){
        while(head != null){
            System.out.print(head.data+" ");
            head = head.next;
        }
        System.out.println();
    }
}

// } Driver Code Ends


/*
Structure of node class is:
class Node {
    char data;
    Node next;
    
    public Node(char data){
        this.data = data;
        next = null;
    }
}
*/
class Solution {
    
    public Node arrangeCV(Node head){
        //write code here and return the head of changed linked list
        
        Node vowels = new Node('a');
        Node consonants = new Node('a');
        
        Node vowHead = vowels, consHead = consonants;
        
        Node temp = head;
        
        while(temp != null){
            
            if(temp.data == 'a' || temp.data == 'e' || temp.data == 'i' || temp.data == 'o' || temp.data == 'u'){
                
                
                    Node vow = new Node(temp.data);
                    vow.next = null;
                    vowels.next = vow;
                    vowels = vowels.next;
            
                
            }else{
                
                    Node cons = new Node(temp.data);
                    cons.next = null;
                    consonants.next = cons;
                    consonants = consonants.next;
                    
                
                
            }
            
            temp = temp.next;
        }
        
        vowels.next = consHead.next;
        
        return vowHead.next;
    }
}