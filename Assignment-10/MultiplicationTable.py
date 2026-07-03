def Multiplication(no):
    
    Result = list()

    for i in range (1,11):
        res = no * i 
        Result.append(res)

    return Result

def main():
    value= int(input("Enter a number : "))

    ret=Multiplication(value)
    print("Multiplication Table is : ",ret)

if __name__ == "__main__":
    main()