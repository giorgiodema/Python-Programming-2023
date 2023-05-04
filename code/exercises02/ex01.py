# write a recursive function that computes the 
# nth power of a number

def pow(base,exp):
    if exp==0:
        return 1.
    res = 1
    while exp > 0:
        res *= base
        exp -= 1
    return res

def recursive_pow(base,exp):
    if exp==0:
        return 1
    else:
        return base * recursive_pow(base,exp-1)
    
if __name__=="__main__":
    base = 2
    exp = 8

    print(f"pow({base},{exp}) = {pow(base,exp)}")
    print(f"recursive_pow({base},{exp})= {recursive_pow(base,exp)}")