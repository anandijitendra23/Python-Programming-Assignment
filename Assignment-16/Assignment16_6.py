def ChkNum(no):

    if (no > 0):
        return "Positive Number"
    
    elif (no < 0):
        return "Negative Number"
    
    else:
        return "Zero"

def main():

    value = int(input("Enter a number : "))

    ret = ChkNum(value)

    print(ret)

if __name__ == "__main__":
    main()