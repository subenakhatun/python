
'''
Write a program to sum of all odd and even index item in that list
Sample input:
L = [1,2,3,4,5,6,7,8,9]
Sample output:
sum_odd_index  = 20
Sum_even_index = 25

'''

l = [1,2,3,4,5,6,7,8,9]
even_number = 0
odd_number = 0

for i in l:
    if i%2 == 0:
        even_number = even_number +i
    elif i%2 == 1:
        odd_number = odd_number + i

print('Sum_even_index = ',even_number)
print('sum_odd_index  =',odd_number)