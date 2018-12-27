'''
Print multiplication table of 14
	Sample Output:
	14 * 1 = 14
	14 * 2 = 28
	.
	.
	.
	.
	.
	.14 *10 = 140

'''
given_number = 14
for i in range(1,11):
    multiple = given_number * i
    print("{0} * {1} = {2}".format(given_number,i,multiple))

