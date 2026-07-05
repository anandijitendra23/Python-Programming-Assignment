Count_Even = lambda no : no % 2 == 0

def main():

    n = int(input("Enter number of elements : "))

    numbers = list()

    for i in range(n):
        no = int(input("Enter number :"))
        numbers.append(no)

    FData = list(filter(Count_Even,numbers))
    print("List of Even Numbers is : ",FData)

    print("Count of Even Numbers in the List is : ",len(FData))

if __name__ == "__main__":
    main()
