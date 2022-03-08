
def swap_without_using_third_variable(a,b, operator):

    if ( operator == 'add_subtract'):
        a = a + b
        b = a - b
        a = a - b
        return a ,b

    if ( operator == 'mul_divide'):
        a = a * b
        b = a / b
        a = a / b
        return int(a), int(b)

a = 10
b = 20

print( "Before Swap " )
print("a = > "+ str(a) )
print("b = > "+ str(b) )
print()
a, b = swap_without_using_third_variable(a,b, 'mul_divide')
a, b = swap_without_using_third_variable(a,b, 'add_subtract')

print( "After Swap " )
print("a = > "+ str(a) )
print("b = > "+ str(b) )
print()
