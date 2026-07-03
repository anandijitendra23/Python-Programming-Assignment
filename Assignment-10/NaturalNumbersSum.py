def SumofNaturalNumbers(no):
    Sum = 0

    for i in range (no+1):
        Sum = Sum + i
         
    return Sum

def main():

    value = (int(input("Enter a number : ")))

    ret = SumofNaturalNumbers(value)
    print("The sum of natural numbers is : ",ret)

if __name__ == "__main__" :
    main()