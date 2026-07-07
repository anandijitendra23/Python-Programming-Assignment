def MinList(Num):

    min = Num[0]

    for i in Num:
        if i < min:
            min = i 
    return min

def main():

    numbers = list()

    n = int(input("Enter number of elements : "))

    for i in range (n):
        no = int(input("Enter Elements : "))
        numbers.append(no)

    ret = MinList(numbers)

    print("Minimun number from the list is : ",ret)

if __name__ == "__main__":
    main()