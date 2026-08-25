'''n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
* * * * *
*       *
*       *
*       *
* * * * * 


n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
* * * * * 
*       * 
* * * * * 
*       * 
* * * * * 


n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
* * * * * 
*         
* * * * * 
*         
* * * * * 


n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
* * * * * 
*         
*         
*         
* * * * * 


n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
* * * * * 
*         
* * * * * 
*         
*

n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i>=m) or (j==n-1 and i>=m) or i==m or (i+j==m and i<=m) or (j-i==m and i<=m) or (i==n-1 and i<=m) or i+j==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

7
      *       
    *   *     
  *       *   
* * * * * * * 
*           * 
*           * 
*           * 


n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or(j==n-1 and i>=m) or(i==m and j>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
* * * * * 
*         
*   * * * 
*       * 
* * * * * 


n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
*       * 
*       * 
* * * * * 
*       * 
*       * 


n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
* * * * * 
    *     
    *     
    *     
* * * * * 

n=int(input())
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

7
*           * 
  *       *   
    *   *     
      *       
    *   *     
  *       *   
*           * 


n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m or (i==n-1 and j<=m) or (j==0 and i>m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
* * * * * 
    *     
    *     
*   *     
* * *  
'''


'''
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
* * * * * 
      *   
    *     
  *       
* * * * * 


n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and i<=2) or (i+j==n-1 and i<=m) or (j==m and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

7
*           * 
  *       *   
    *   *     
      *       
      *       
      *       
      * 

n=int(input())
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
*         
*         
*         
*         
* * * * * 

n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i<=m) or (i+j==n-1 and i<=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

7
*           * 
* *       * * 
*   *   *   * 
*     *     * 
*           * 
*           * 
*           * 


n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i>=m) or (i+j==n-1 and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
7
*           * 
*           * 
*           * 
*     *     * 
*   *   *   * 
* *       * * 
*           * 


n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or (i+j==n-1 and i<=m) or (i==m and j<=m) or (i==j and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
*       * 
*     *   
* * *     
*     *   
*       * 


n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m) or i-j==m or i+j==n+m-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

7
*           * 
*           * 
*           * 
*           * 
  *       *   
    *   *     
      *  


n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (i+j==n-1 and i<=m) or (i==m and j<=m) or (i==j and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
* * * * * 
*     *   
* * *     
*     *   
*       * 


n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or (j==0 and i<=m) or i==n-1 or (j==n-1 and i>=m) or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
* * * * * 
*         
* * * * * 
        * 
* * * * * 


n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or (i==j and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

5
* * * * * 
*       * 
*   *   * 
*     * * 
* * * * *
'''
