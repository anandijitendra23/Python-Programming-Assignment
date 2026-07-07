def CountDigits(no):
    count = 0

    while no != 0:
        count = count + 1
        no = no // 10

    return count

def main():

    num = int(input("Enter a number : "))

    ret = CountDigits(num)

    print("Number of digits are : ",ret)

if __name__ == "__main__":
    main()