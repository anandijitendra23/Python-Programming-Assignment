def Cube(no):

    res = no*no*no
    return res

def main():

    value = int(input("Enter a number : "))
    
    ret = Cube(value)
    print("Cube of the given number is : ",ret)

if __name__ == "__main__":
    main()