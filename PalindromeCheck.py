

def palindrome_check(palindrome):

    count = int(len(palindrome)/2)
    index = 0

    while(count>0):
        if palindrome[len(palindrome)- 1 -index] != palindrome[index]:
            return False
        index += 1
        count -= 1
    return True

palindrome = input("Enter the string: ")

if palindrome_check(palindrome):
    print("The given string " + str(palindrome) +" is plaindrome! ")
else:
    print("The given string " + str(palindrome) +" is not palindrome! ")