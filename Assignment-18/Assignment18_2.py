def MaxList(Num):

    max = Num[0]

    for i in Num:
        if i > max:
            max = i 
    return max

def main():

    numbers = list()

    n = int(input("Enter number of elements : "))

    for i in range (n):
        no = int(input("Enter Elements : "))
        numbers.append(no)

    ret = MaxList(numbers)

    print("Maximum number from the list is : ",ret)

if __name__ == "__main__":
    main()