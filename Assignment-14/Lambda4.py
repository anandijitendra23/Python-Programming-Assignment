MinimumValue = lambda no1,no2 : min(no1,no2)

def main():
     
     no1 = int(input("Enter first number : "))
     no2 = int(input("Enter second number : "))

     ret = MinimumValue(no1,no2)
     print("Minimum Value is : ",ret)

if __name__ == "__main__":
    main()