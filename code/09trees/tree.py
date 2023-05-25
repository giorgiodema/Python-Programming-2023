import string
from typing import Callable
from pathlib import Path

class Node:
    """
    Simple implementation of the binary tree. Each node has a pointer to the right and 
    left children (or None if it has no children) and a value.
    """
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

def read_tree(path):
    """
    Instantiate a binary tree from the graphical 2D representation given as a 
    txt file. The representaiton must follows these rules:
    -> left links are represented with '/' and right links with '\\' characters
    -> the left link starts one cell below on the left  with respect to the root
    -> the right link starts one cell below on the right with respect to the root
    -> the left link ends one cell above on the right with respect to the left child
    -> the right link ends one cell above on the left with respect to the right child
    -> each level of the tree occupies a single row in the file
    See files ex01.txt, ex02.txt, ex03.txt for valid examples
    """
    f = open(path,"r")
    root = None

    it = iter(f)
    try:
        parents = list(next(it))
        parents = [(i,x) for i,x in enumerate(parents)]
        parents = list(filter(lambda x: x[1].isalnum(),parents))
        # each element of the list is a tuple containing the parent node and
        # the estimated positions of left and right children (respectively 
        # one cell below on the left and one cell below on the right with respect
        # to the parent)
        parents = [(Node(x[1],None,None),x[0]-1,x[0]+1) for x in parents]
        # assign the root node to root
        root = parents[0][0]
        # continue reading untill the end of the file
        while True:
            # for each row without nodes (just links) update the positions of 
            # left and right children of parent nodes. If the parent has no links
            # then set the position of the corresponding children to zero
            links = list(next(it))
            while len(list(filter(lambda x:x.isalnum(),links)))==0:
                parents = [(e[0],e[1]-1 if e[1] else None,e[2]+1 if e[2] else None) for e in parents]
                for i in range(len(parents)):
                    if parents[i][1]!=None:
                        if len(links)<=parents[i][1]+1 or links[parents[i][1]+1]!="/":
                            parents[i] = (parents[i][0],None,parents[i][2])
                    if parents[i][2]!=None:
                        if len(links)<=parents[i][2]-1 or links[parents[i][2]-1]!="\\":
                            parents[i] = (parents[i][0],parents[i][1],None)
                links = list(next(it))

            # now read the children and assign the left and right pointers of the
            # parents to the corresponding childrens
            childrens = links
            childrens = [(i,x) for i,x in enumerate(childrens)]
            childrens = list(filter(lambda x: x[1].isalnum(),childrens))
            childrens = [(Node(x[1],None,None),x[0]-1,x[0]+1) for x in childrens]
            for p in parents:
                left  = list(filter(lambda c:p[1]==c[1]+1,childrens)) if p[1]!=None else None
                right = list(filter(lambda c:p[2]==c[2]-1,childrens)) if p[2]!=None else None
                left = left[0][0] if left else None
                right = right[0][0] if right else None
                p[0].left = left
                p[0].right = right
            parents = childrens

    except StopIteration:
        f.close()
        return root
    

def dfs(root:Node,order:string,visit_fn:Callable):
    """
    Implements the depth-first-search on the binary tree. 
    In depth-first search (DFS), the search tree is deepened 
    as much as possible before going to the next sibling.
    The order specifies the order of the visit:
        -> inorder:  visit the deepest node on the left, then go up,
                     visit the node and then go to the right
        -> preorder: visit the current node, then go to the left, then to
                     the right 
        -> postorder: visit the deepest node on the left, then visit the right 
                      sibling, and then visit the parent
    """
    
    if order not in ["inorder", "preorder", "postorder"]:
        raise ValueError("Unknown order, accepted values for order are: inorder | preorder | postorder ")
    
    if order == "inorder":
        if root.left:
            dfs(root.left,order,visit_fn)
        visit_fn(root)
        if root.right:
            dfs(root.right,order,visit_fn)

    elif order == "postorder":
        if root.left:
            dfs(root.left,order,visit_fn)
        if root.right:
            dfs(root.right,order,visit_fn)
        visit_fn(root)
    
    else:
        visit_fn(root)
        if root.left:
            dfs(root.left,order,visit_fn)
        if root.right:
            dfs(root.right,order,visit_fn)



if __name__=="__main__":
    root = read_tree(Path(__file__).with_name("ex03.txt"))
    print("In-order")
    dfs(root,"inorder",lambda x:print(f"{x.value} -> ",end=""))
    print("\nPre-order")
    dfs(root,"preorder",lambda x:print(f"{x.value} -> ",end=""))
    print("\nPost-order")
    dfs(root,"postorder",lambda x:print(f"{x.value} -> ",end=""))
    print()