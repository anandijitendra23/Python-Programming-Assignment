def Factors_Add(no):

    sum = 0

    for i in range(1,no):
        if ( no % i ==0):
            sum = sum + i
    return sum

def main():

    value = int(input("Enter a number : "))

    ret = Factors_Add(value)

    print(f"Addition of Factors of {value} = ",ret)

if __name__ == "__main__":
    main()