def Binary(no):
    binary = ""

    while no > 0:
        num = no % 2
        binary = str(num) + binary
        no = no // 2

    return binary

def main():
    
    value = int(input("Enter a number : "))

    ret = Binary(value)
    print("Binary : ",ret)


if __name__ == "__main__":
    main()