

def linear_search(l,elem):
    for e in l:
        if e == elem:
            return True
    return False

def binary_search(l,elem):
    # base case
    if len(l)==1:
        if l[0]==elem:
            return True
        else:
            return False
    m = len(l)//2
    if elem == l[m]:
        return True
    # inductive step
    elif elem > l[m]:
        return binary_search(l[m:],elem)
    else:
        return binary_search(l[0:m],elem)

if __name__=="__main__":
    l = [1,3,5,8,9,11,15,17,22,45,67,81,99]
    print(f"linear_search(l,67) = {linear_search(l,67)}")
    print(f"linear_search(l,100) = {linear_search(l,100)}")
    print(f"binary_search(l,67) = {binary_search(l,67)}")
    print(f"binary_search(l,100) = {binary_search(l,100)}")
    