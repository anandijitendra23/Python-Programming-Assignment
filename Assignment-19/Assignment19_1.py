Power = lambda no : 2 ** no

def main():

    value = int(input("Enter a number : "))

    ret = Power(value)
    print("Output : ",ret)

if __name__ == "__main__":
    main()
