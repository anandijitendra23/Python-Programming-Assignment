MaximumValue = lambda no1,no2,no3 : max(no1,no2,no3)           

def main():

    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    no3 = int(input("Enter third number : "))

    ret = MaximumValue(no1,no2,no3)
    print("Maximum value is : ",ret)

if __name__ == "__main__":
    main()

