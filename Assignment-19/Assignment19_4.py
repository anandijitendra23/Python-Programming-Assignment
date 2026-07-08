from functools import reduce

ChkEven = lambda no : no % 2 == 0
SquareEven = lambda no : no * no
Sum = lambda no1 , no2 : no1 + no2 

def main():

    num_list = list()

    n = int(input("Enter number of elements to enter : "))

    for i in range(n):
        no = int(input("Enter element : "))
        num_list.append(no)

    FData = list(filter(ChkEven , num_list))
    print("List after Filter : ",FData)

    MData = list(map(SquareEven , FData))
    print("List after Map : ",MData)

    RData = reduce(Sum , MData)
    print("Reduce : Addition is = ",RData)

if __name__ == "__main__":
    main()