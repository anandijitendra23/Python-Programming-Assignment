MaximumValue = lambda no1,no2 : max(no1,no2)           # no1 if no1 > no2 else no2

def main():

    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    ret = MaximumValue(no1,no2)
    print(f"Maximum value is : ",ret)

if __name__ == "__main__":
    main()