# Write a function that takes a list of numbers, 
# a starting base b1 and a target base b2 and interprets 
# the list as a number in base b1 and converts it into a 
# number in base b2 (in the form of a list-of-digits). 
# So for example [2,1,0] in base 3 gets converted to base 10 as [2,1]
# and to base 2 as [1,0,1,0,1]

# input
b1 = 3
b2 = 10
n1 = [2,1,0]

# program
ndec = 0
for i in range(1,len(n1) + 1):
    ndec += n1[-i] * b1 ** (i-1)

n2 = []
while ndec > 0:
    n2.append(ndec % b2)
    ndec = ndec // b2
n2 = n2[::-1]

# print output
print(n2)