def Palindrome(no):

    temp = no
    rev = 0

    while no > 0 :
        digit = no % 10
        rev = rev * 10 + digit
        no = no // 10

    if temp == rev :
        return True
    else :
        return False

def main():

    value = int(input("Enter a number : "))

    ret = Palindrome(value)

    if Palindrome(value):
        print("It is a Palindrome.")
    else:
        print("Not a Palindrome.")



if __name__ == "__main__":
    main()