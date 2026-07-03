def ChkGreater(no1,no2):

    if no1>no2:
        return no1
    else:
        return no2

def main():

    value1=int(input("Enter first number : "))
    value2=int(input("Enter second nnumber : "))
    
    ret=ChkGreater(value1,value2)
    print("Greater number is : ",ret)

if __name__ == "__main__":
    main()