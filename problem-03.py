'''
Write a Python program to multiply all the items in a list
	Sample input:
L = [1,2,3,4,5,]
Sample output: 120

'''

l = [1,2,3,4,5]
mul = 1
for i in l:
    mul = mul * i
print(mul)