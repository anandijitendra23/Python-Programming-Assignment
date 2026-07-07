def is_Prime(no):

    if no <= 1:
        return False
    
    for i in range(2,no):
        if no % i == 0:
            return False
    
    return True

def main():
    
    value = int(input("Enter a number : "))

    ret = is_Prime(value)

    if (ret == True):
        print("It is Prime Number")

    else:
        print("It is not a Prime Number")

if __name__ == "__main__":
    main()