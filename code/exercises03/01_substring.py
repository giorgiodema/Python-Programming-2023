
def is_substring(s:str,sub:str):
    # base cases
    if len(s)<len(sub):
        return False
    if s[0:len(sub)] == sub:
        return True
    else:
        return is_substring(s[1:],sub)
    
print(f"is_substring('hello world','llo') = {is_substring('hello world','llo')}")
print(f"is_substring('hello world','') = {is_substring('hello world','')}")
print(f"is_substring('hello world','a') = {is_substring('hello world','a')}")
print(f"is_substring('hello world','world!') = {is_substring('hello world','world!')}")