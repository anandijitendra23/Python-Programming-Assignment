def is_Divisibleby5(no):

    if (no % 5 == 0):
        return True
    else:
        return False
    
def main():

    value = int(input("Enter a number : "))

    ret = is_Divisibleby5 (value)

    print(ret)

if __name__ == "__main__":
    main()