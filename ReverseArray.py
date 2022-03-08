
def reverseArray(a):
    # Write your code here
    iterations = int(len(a) / 2)

    index = 0
    while (iterations > 0):
        temp = a[index]
        a[index] = a[len(a) - 1 - index]
        a[len(a) - 1 - index] = temp
        index += 1
        iterations -= 1

    return a

a = [4,6,7,8,9,10]
b = reverseArray(a)
print(b)
