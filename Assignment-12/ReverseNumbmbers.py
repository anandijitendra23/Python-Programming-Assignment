def ReverseNumbers(no):

    return range (no,0,-1)

def main():

    value = int(input("Enter a number : "))

    ret = ReverseNumbers(value)

    print("Numbers : ",ret)
    for i in ret :
        print(i)

if __name__ == "__main__":
    main()