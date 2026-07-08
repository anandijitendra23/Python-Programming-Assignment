Mult = lambda no1 ,no2 : no1 * no2

def main():

    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))

    ret = Mult(value1 , value2)

    print(f"Multiplication : {value1} * {value2} : ",ret)

if __name__ == "__main__":
    main()