def Odd(no):

    result = []

    for i in range(1,no+1):
        if (i % 2 != 0):
            result.append(i)

    return result

def main():

    value = int(input("Enter a number : "))

    ret = Odd(value)
    print("Odd Numbers are : ",ret)
                

if __name__ == "__main__":
    main()