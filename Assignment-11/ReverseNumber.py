def Reverse(no):
    rev = 0

    while no > 0:
        digit = no % 10
        rev = rev * 10 + digit
        no = no // 10

    return rev

def main():

    value = int(input("Enter a number : "))

    ret = Reverse(value)
    print("Reverse of the number is : ",ret)


if __name__ == "__main__":
    main()