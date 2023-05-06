# Write a program that merges two sorted lists into a new sorted list. 
# [1,4,6],[2,3,5] → [1,2,3,4,5,6]. You can do this quicker than 
# concatenating them followed by a sort

# input
l1 = [1,3,3,5,7,8,9,13,14]
l2 = [0,4,5,10]

# program
l_new = []
l1id = 0
l2id = 0
while l1id < len(l1) and l2id < len(l2):
    if l1[l1id] <= l2[l2id]:
        l_new.append(l1[l1id])
        l1id += 1
    else:
        l_new.append(l2[l2id])
        l2id += 1

if l1id == len(l1) and l2id < len(l2):
    l_new = l_new + l2[l2id:]
elif l2id == len(l2) and l1id < len(l1):
    l_new = l_new + l1[l1id:]

# print output
print(l_new)