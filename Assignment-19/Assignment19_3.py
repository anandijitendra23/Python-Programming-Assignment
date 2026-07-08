from functools import reduce

ChkGreater = lambda no : no >= 70 and no <= 90 
Increment = lambda no : no + 10
Product = lambda no1 , no2 : no1 * no2

def main():

    num_list = list()

    n = int(input("Enter number of elements : "))

    for i in range (n):
        no = int(input("Enter Elements : "))
        num_list.append(no)

    FData = list(filter(ChkGreater , num_list))
    print("List after filter : ",FData)

    MData = list(map(Increment , FData))
    print("List after Map : ",MData)

    RData = reduce(Product , MData)
    print("Product of all elements in list after reduce : ",RData)

if __name__ == "__main__":
    main()