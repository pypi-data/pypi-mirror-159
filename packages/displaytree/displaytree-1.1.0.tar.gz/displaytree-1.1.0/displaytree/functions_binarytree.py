#B PRAJEETH

def display(root,right,left,val,n,ar,y,x,max_width):
    if root:
        ar[2*y][x-1]=getattr(root,val)
        if(len(str(getattr(root,val))) > max_width[0]):
            max_width[0] = len(str(getattr(root,val)))        
        
        if(n > y+1):
            for i in range(1, (2**(n-y-2)) +1):
                ar[2*y][x-1+i]="_"
                ar[2*y][x-1-i]="_"
            ar[2*y +1][x-1 - (2**(n-y-2))]="|"
            ar[2*y +1][x-1 + (2**(n-y-2))]="|"
        y=y+1
        if(y <= n-1):
            ar[2*y][x-1 - (2**(n-y-1)) ]="?"
            ar[2*y][x-1 + (2**(n-y-1)) ]="?" 
            
        display(getattr(root,left),right,left,val,n,ar,y,x-(2**(n-y-1)),max_width)
        display(getattr(root,right),right,left,val,n,ar,y,x+(2**(n-y-1)),max_width)
        y=y-1
 
def height(node, right, left):  #function to calculte the maximum height of a tree
    '''
    Helps you identify the height of the node which we require
    
    example: print(height(node, "right", "left"))

    height(node, "right", "left") - will return the height of the node.
    '''
    if node is None:
        return -1 
 
    else :

        lDepth = height(getattr(node,left), right, left)
        rDepth = height(getattr(node,right), right, left)

        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1  

def binarytree(r,right,left,val):
    '''
    This function helps you visualize binary trees .

    Pass these three attributes and the root node of the tree as arguements.

    Example: binarytree(root, "right", "left", "value")

    Parameters: 4 parameters required.

    1. root - object of node class.

    2. right - pointer attribute to the right node, passed as string.

    3. left - pointer attribute to the left node, passed as string.

    4. value - data attribute to printed in each node, passed as string.  
    '''
    ar=[]
    n=height(r, right, left) +1 # height of tree
    for i in range(2*n):
      ls=[]
      for j in range((2**n)-1):
        ls.append("")
      ar.append(ls)    
    
    y=0
    x=2**(n-y-1)
    #print("printing tree ... \n")
    max_width=[0]
    display(r,right,left,val,n,ar,y,x,max_width)
    
    for i in range(2*n):
        ct=0
        ct1=0
        for j in range((2**n)-1):
            if(ar[i][j]==""):
                print(" "*max_width[0],end="")
            else:
                width=max_width[0] - len(str(ar[i][j]))
                if(ar[i][j] != "_" and ar[i][j]!="?" and ar[i][j]!="|" and width>0):
                    ct1 = ct1 +1
                    if(i != 2*n - 2):
                        if(ct1%2 == 0):
                            print("_"*(width) + str(ar[i][j]),end="")
                        else:
                            print(str(ar[i][j]) + "_"*(width) ,end="")
    
                    else:  
                        if(ct1%2 == 0):
                            print(" "*(width) + str(ar[i][j]),end="")
                        else:
                            print(str(ar[i][j])+" "*(width) ,end="")   
                elif(ar[i][j]=="?"):
                    ct1=ct1+1
                    if(ct1 %2 == 0):
                        print(" "*width + str(ar[i][j]),end="")  
                    else:
                        print(str(ar[i][j]) + " "*width ,end="")  
                elif(ar[i][j] == "_"):
                    print(ar[i][j]*max_width[0],end="")
                else:
                    ct=ct+1
                    if(ct%2 == 0):
                        print(" "*(width) + str(ar[i][j]),end="") 
                    else:
                        print(str(ar[i][j]) + " "*(width),end="")   

        print()   



