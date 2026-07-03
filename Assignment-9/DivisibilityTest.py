def Divisible(no):

    if no % 3 == 0 and no % 5 == 0:
        return True
    else:
        return False


def main():
    value = int(input("Enter a number : "))

    ret = Divisible(value)
    
    if ret == True:
        print("Divisible by 3 and 5")
    else:
        print("Not diivisible by 3 and 5")


if __name__ == "__main__":
    main()