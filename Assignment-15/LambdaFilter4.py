Divisiblity_Test = lambda no : no % 3 == 0 and no % 5 == 0

def main():

    n = int(input("Enter number of elements : "))

    numbers_list = list()

    for i in range(n):
        no = int(input("Enter number :"))
        numbers_list.append(no)

    FData = list(filter(Divisiblity_Test,numbers_list))
    print("List of Odd Numbers is : ",FData)

if __name__ == "__main__":
    main()
