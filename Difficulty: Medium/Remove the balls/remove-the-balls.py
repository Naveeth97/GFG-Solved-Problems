#User function Template for python3

class Ball:
    
    def __init__(self, col, rad):
        
        self.col = col;
        self.rad = rad;
        
class Solution:
    def findLength(self, color, radius):
        
        lis = []
        
        for i in range(len(color)):
            
            if len(lis) > 0:
                
                top_element = lis[-1]
                
                if top_element.col == color[i] and top_element.rad == radius[i]:
                    lis.pop()
                else:
                    lis.append(Ball(color[i], radius[i]))
            else :
                
                lis.append(Ball(color[i], radius[i]))
        
        return len(lis)
            
            
        
        