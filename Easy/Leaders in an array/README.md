<h2><a href="https://www.geeksforgeeks.org/problems/leaders-in-an-array--170647/1?page=1&category=Arrays,Strings,Linked%20List&company=Amazon,Microsoft,Flipkart,Adobe,Google,Samsung,MakeMyTrip,Zoho,Paytm,Walmart,Goldman%20Sachs,Morgan%20Stanley,OYO%20Rooms,D-E-Shaw,Oracle,Facebook,VMWare,SAP%20Labs,Cisco,Linkedin,Yahoo,Wipro,Salesforce,TCS,Twitter,Atlassian,Infosys,Uber&sprint=bookmark&sortBy=latest">Leaders in an array</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array A of positive integers. Your task is to find the leaders in the array.&nbsp;An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader.&nbsp;</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>n = 6
A[] = {16,17,4,3,5,2}
<strong>Output: </strong>17 5 2<strong>
Explanation: </strong>The first leader is 17 
as it is greater than all the elements
to its right.&nbsp; Similarly, the next 
leader is 5. The right most element 
is always a leader so it is also 
included.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>n = 5
A[] = {1,2,3,4,0}
<strong>Output: </strong>4 0
<strong>Explanation: </strong>The first leader is 4
as all the other numbers aren't greater than
the other elements to their right side.
The second leader is 0 as there are no elements
at right side so its greater itself.</span>
</pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything.&nbsp;The task is to complete the function <strong>leader</strong>() which takes array A and n&nbsp;as input parameters and&nbsp;returns an array of leaders in order of their appearance.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong></span><span style="font-size:18px">&nbsp;O(n)</span><br>
<span style="font-size:18px"><strong>Expected Auxiliary Space:</strong>&nbsp;O(n)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= n&nbsp;&lt;= 10<sup>5</sup><br>
0 &lt;= A<sub>i</sub> &lt;= 10<sup>9</sup></span></p>
</div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Payu</code>&nbsp;<code>Adobe</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;