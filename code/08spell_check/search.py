from typing import List,Callable
import sys

def find_first_binary_search(l:List,elem:object,cmp:Callable)->int:
    """
    finds the first occurence of elem in an ordered sequence 
    and returns its index, it returns an arbitrary 
    negative value if the element is not found. cmp 
    is the function used to compare the elements, it 
    should return 0 if the elements are equal, -1 if 
    they are in the right order or +1 otherwise
    """
    # base case
    if len(l)==0:
            return -sys.maxsize
    m = len(l)//2
    if (m==0 or cmp(l[m-1],elem)<0) and cmp(elem,l[m])==0:
        return m
    # inductive step
    elif cmp(elem,l[m])>0:
        return m + 1 + find_first_binary_search(l[m+1:],elem,cmp)
    else:
        return 0 + find_first_binary_search(l[0:m],elem,cmp)
    
def find_last_binary_search(l:List,elem:object,cmp:Callable)->int:
    """
    finds the last occurence of elem in an ordered sequence
    and returns its index, it returns an arbitrary 
    negative value if the element is not found. cmp 
    is the function used to compare the elements, it 
    should return 0 if the elements are equal, -1 if 
    they are in the right order or +1 otherwise
    """
    # base case
    if len(l)==0:
            return -sys.maxsize
    m = len(l)//2
    if (m==(len(l)-1) or cmp(elem,l[m+1])<0) and cmp(elem,l[m])==0:
        return m
    # inductive step
    elif cmp(elem,l[m])>=0:
        return m + 1 + find_last_binary_search(l[m+1:],elem,cmp)
    else:
        return 0 + find_last_binary_search(l[0:m],elem,cmp)