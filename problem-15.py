'''
Print the following patterns using loop :

*
**
***
****

'''
n = 5
for i in range(n):
    for j in range(i):
        print("*",end='')
    print('')