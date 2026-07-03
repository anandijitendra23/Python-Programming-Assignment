def Operations(no1,no2):

    Addition = no1 + no2
    Substraction = no1 - no2
    Multiplication = no1 * no2
    Division = no1 / no2

    return Addition,Substraction,Multiplication,Division
    

def main():

    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))

    add,sub,mul,div = Operations(num1,num2)

    print("Addition is : ",add)
    print("Subtraction is : ",sub)
    print("Multiplication is : ",mul)
    print("Division is : ",div)
    

if __name__ == "__main__":
    main()