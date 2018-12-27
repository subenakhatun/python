'''
Take two inputs from user and check whether they are equal or not.
'''

a = int(input('Enter first number: '))
b = int(input("Enter seconf number: "))

if a == b:
    print('they ar similar')
elif a > b:
    print('{0} is greater then {1}'.format(a,b))
elif a < b:
    print('{0} is smaller then {1}'.format(a, b))
