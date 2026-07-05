from functools import reduce

Addition = lambda no1,no2 : no1 + no2

def main():

    n = int(input("Enter number of elements : "))

    numbers = list()

    for i in range(n):
        no = int(input("Enter number :"))
        numbers.append(no)

    RData = reduce (Addition , numbers)
    print("Addition of elements is : ",RData)

if __name__ == "__main__":
    main()