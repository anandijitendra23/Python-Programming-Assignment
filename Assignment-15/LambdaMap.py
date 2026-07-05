Square = lambda no : no*no

def main():

    n = int(input("Enter number of elements : "))

    numbers = list()

    for i in range(n):
        no = int(input("Enter number :"))
        numbers.append(no)

    MData = list(map(Square,numbers))
    print("List of Squared Numbers is : ",MData)

    
if __name__ == "__main__":
    main()