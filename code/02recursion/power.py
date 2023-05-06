def pow(base,exp):
    # base case
    if exp==0:
        return 1
    # inductive case
    else:
        ret =  base * pow(base,exp-1)
        return ret
    

print(pow(2,4))