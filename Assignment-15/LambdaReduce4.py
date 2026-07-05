from functools import reduce

Product = lambda no1,no2 : no1*no2

def main():

    n = int(input("Enter number of elements : "))

    numbers = list()

    for i in range(n):
        no = int(input("Enter number : "))
        numbers.append(no)

    RData = reduce (Product , numbers)
    print("Product of alla elements in the list is : ",RData)
    

if __name__ == "__main__":
    main()
