def ChkNum(no):

    if (no % 2 == 0):
        return True
    else:
        return False

def main():

    value = int(input("Enter a number : "))

    ret = ChkNum(value)

    if (ret == True):
        print("Even Number ")

    else:
        print("Odd Number")

if __name__ == "__main__":
    main()