def PrintNumbers(no):

    return range (1,no+1)

def main():

    value = int(input("Enter a number : "))

    ret = PrintNumbers(value)

    print("Numbers : ",ret)
    for i in ret :
        print(i)

if __name__ == "__main__":
    main()