Addition = lambda no1,no2 : no1+no2

def main():

    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    ret = Addition(no1,no2)
    print(f"Addition of {no1} and {no2} is : ",ret)
    
if __name__ == "__main__":
    main()