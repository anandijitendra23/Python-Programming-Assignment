def SumList(num):

    sum = 0 

    for ele in num:
        sum = sum + ele 

    return sum

def main():

    numbers = list()

    n = int(input("Enter number of elements : "))

    for i in range (n):
        no = int(input("Enter Elements : "))
        numbers.append(no)

    ret = SumList(numbers)

    print("Sum of all elements in the list is : ",ret)

if __name__ == "__main__":
    main()