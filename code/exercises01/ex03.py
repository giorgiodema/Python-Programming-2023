# Write a function that rotates a list by k elements. 
# For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2]. 
# Try solving this without creating a copy of the list. 
# How many swap or move operations do you need?

# input
l = [1,2,3,4,5,6]
k = 2

# program (creating a new list)
l_new = []
for i in range(len(l)):
    l_new.append(l[(i + k) % len(l)])
# print output
print(l_new)

# program (without creating a copy)
for i in range(k):
    l.append(l.pop(0))
# print output
print(l)