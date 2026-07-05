CheckEven = lambda value : value % 2 == 0

def main():

    value = int(input("Enter a number : "))

    ret = CheckEven(value)

    print("Is Even : ",ret)

if __name__ == "__main__":
    main()