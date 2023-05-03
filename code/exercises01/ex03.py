# Write a function that rotates a list by k elements. 
# For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2]. 
# Try solving this without creating a copy of the list. 
# How many swap or move operations do you need?

# input
l = [1,2,3,4,5,6]
k = 2

# program
for i in range(0, len(l) - k):
    a = l[i]
    l[i] = l[i + k % len(l)]
    l[i + k % len(l)] = a

# print output
print(l)

