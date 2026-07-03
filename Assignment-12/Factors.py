def FactorsofNumber(no):
    fact = []

    for i in range (1,no+1):
        if no % i == 0:
            fact.append(i)
    
    return fact
        
def main():

    value=int(input("Enter a number : "))

    ret = FactorsofNumber(value)
    print("Factors are : ",ret)

if __name__ == "__main__":
    main()