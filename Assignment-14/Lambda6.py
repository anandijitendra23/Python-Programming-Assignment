CheckOdd = lambda value : value % 2 == 1

def main():

    value = int(input("Enter a number : "))

    ret = CheckOdd(value)

    print("Is Odd : ",ret)

if __name__ == "__main__":
    main()