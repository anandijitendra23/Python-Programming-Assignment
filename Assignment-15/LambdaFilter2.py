OddNumbers = lambda no : no % 2 == 1

def main():

    n = int(input("Enter number of elements : "))

    numbers = list()

    for i in range(n):
        no = int(input("Enter number :"))
        numbers.append(no)

    FData = list(filter(OddNumbers,numbers))
    print("List of Odd Numbers is : ",FData)

if __name__ == "__main__":
    main()
