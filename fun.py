
# function call
def function_name(parameter1,parameter2):
    sum = parameter1 + parameter2
    return sum
sum = function_name(20,13)

# print(function_name(4,9))
print(sum)

# variable scope, inside variable mane local variable, vitorer bvariable kaj korche
def variable_scope(a,b):
    a = 30
    b = 50
    c = a + b
    return c
variabel = variable_scope(30,11)
print(variabel)

# withwout return,vitore print na kore jodi bahire print kori thahole none ase,
# ar jodi vitore print kori thahole result show kore
def mul(a,b):
    mul = a * b
    print(mul)
mul = mul(6,9)

# variable scope without return
def variable_scope(a,b):
    a = 30
    b = 50
    c = a + b
    print('inside function',c)
variabel = variable_scope(30,11)
print('outside function',variabel)

#
