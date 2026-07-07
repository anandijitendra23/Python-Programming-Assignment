import MarvellousNum

def ListPrime(num):
    sum = 0

    for i in num :
        if MarvellousNum.ChkPrime(i):
            sum = sum + i

    return sum

def main():

    numbers = list()

    n = int(input("Enter number of elements : "))

    for i in range (n):
        no = int(input("Enter Elements : "))
        numbers.append(no)

    ret = ListPrime(numbers)

    print(f"Addition of Prime Numbers in list is : ",ret)

if __name__ == "__main__":
    main()