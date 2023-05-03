# Write program that combines two lists by 
# alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3]

# input
l1 = [1,2,3,4,5,6,7]
l2 = ['a','b','c']

# program
l_new = []
min_len = None
if len(l1) <= len(l2):
    min_len = len(l1)
else:
    min_len = len(l2)

for i in range(min_len):
    l_new.append(l1[i])
    l_new.append(l2[i])

# if one list is longer than the other
# append the remaining elements at the
# end of the new list
if len(l1) > len(l2):
    l_new = l_new + l1[min_len:]
elif len(l2) > len(l1):
    l_new = l_new + l2[min_len:]

# print output
print(l_new)
