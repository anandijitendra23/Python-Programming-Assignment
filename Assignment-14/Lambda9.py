Multiplication = lambda no1,no2 : no1 * no2

def main():

    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    ret = Multiplication(no1,no2)
    print(f"{no1} multiply by {no2} is : ",ret)

if __name__ == "__main__":
    main()