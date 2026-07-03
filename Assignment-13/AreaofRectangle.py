def AreaofRectangle(len,bth):

    area = len * bth
    return area

def main():

    length = int(input("Enter length of rectangle : "))
    breadth = int(input("Enter breadth of rectangle : "))

    ret = AreaofRectangle(length,breadth)
    print("Area of Rectangle is : ",ret)

if __name__ == "__main__":
    main()