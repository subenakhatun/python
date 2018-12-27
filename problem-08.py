'''
Write a Python program to count the number of elements in a list
	Sample input:
L = [1,2,3,4,5,5,2,2,2]
Check_valu = 5
Sample output:02
If check_valu = 14
Sample output:02
Not found in this list

'''

l = [1,2,3,4,5,5,2,2,2]
check_value = int(input('enter a number for check: '))
if check_value == l:
    print(l.count(check_value))
else:
    print('Not found in this list')
