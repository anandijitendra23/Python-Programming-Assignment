from functools import reduce
MaxValue = lambda no1,no2 : max(no1,no2)

def main():

    n = int(input("Enter number of elements : "))

    numbers = list()

    for i in range(n):
        no = int(input("Enter number :"))
        numbers.append(no)

    RData = reduce (MaxValue , numbers)
    print("Maximum Value is : ",RData)

if __name__ == "__main__":
    main()