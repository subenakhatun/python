'''
Write a Python program to print all odd and even numbers between a given range:
	Sample input:
	Range_val = 10
Sample output:
Odd_numbers:1,3,5,7,9
Even_numbers:2,4,6,8,10

'''
even_number = []
odd_number = []
for i in range(10):
    if i%2==0:
        even_number.append(i)
    elif i%2 == 1:
        odd_number.append(i)
print('Even_numbers: ',even_number)
print('Odd_numbers: ',odd_number)



