# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    matrix = [[0]*(W+1) for x in range(n)]
    
    # Build matrix[][] 
    for i in range(n):
        for w in range(W+1):
            if w==0:
                matrix[i][w]=0   
            elif wt[i] <= w:
                
                matrix[i][w] = max(val[i] + matrix[i-1][w-wt[i]],  matrix[i-1][w])
            else:
                matrix[i][w] = matrix[i-1][w]
                
    return matrix[i][w]
 
# Driver program to test above function
val = [4,1,5,7]
wt = [3,1,4,5]
W = 7
n = len(val)
print(knapSack(W, wt, val, n))
 

