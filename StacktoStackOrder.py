

# Python program to
# demonstrate stack tranfer in order

#stack using list
stack = []
stack_2 = []

for i in range(5):
    stack.append(i+1)

print('Initial stack')
print("Stack 1: " + str(stack))
print("Stack 2: " + str(stack_2))


def in_order_stack_transfer(stack1, stack2):
    if not stack1:
        return
    temp = stack1.pop()
    in_order_stack_transfer(stack1,stack2)
    stack2.append(temp)

in_order_stack_transfer(stack,stack_2)

print('Final stack')
print("Stack 1: " + str(stack))
print("Stack 2: " + str(stack_2))





