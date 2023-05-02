# Write a function that takes a number and returns a list of its digits. 
# So for 2342 it should return [2,3,4,2]

# input
n = 2342

# program
s = str(n)
l = []
for c in s:
    l.append(int(c))

# print output
print(l)
