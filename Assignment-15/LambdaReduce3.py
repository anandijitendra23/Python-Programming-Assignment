from functools import reduce
MinValue = lambda no1,no2 : min(no1,no2)

def main():

    n = int(input("Enter number of elements : "))

    numbers = list()

    for i in range(n):
        no = int(input("Enter number :"))
        numbers.append(no)

    RData = reduce (MinValue , numbers)
    print("Minimum Value is : ",RData)

if __name__ == "__main__":
    main()