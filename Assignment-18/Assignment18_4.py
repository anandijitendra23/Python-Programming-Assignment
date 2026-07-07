def Frequency(num , s):
    count = 0

    for i in num: 
        if i == s :
            count = count +1
    return count


def main():

    numbers = list()

    n = int(input("Enter number of elements : "))

    for i in range (n):
        no = int(input("Enter Elements : "))
        numbers.append(no)

    search = int(input("Enter element to search : "))

    ret = Frequency(numbers , search)

    print(f"Frequency of {search} is : ",ret)

if __name__ == "__main__":
    main()