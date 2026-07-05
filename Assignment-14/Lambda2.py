Cube = lambda no : no*no*no

def main():

    value = int(input("Enter a number : "))

    ret = Cube(value)
    print(f"Cube of {value} is : ",ret)

if __name__ == "__main__":
    main()