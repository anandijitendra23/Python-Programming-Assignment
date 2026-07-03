def AreaofCircle(r):

    PI = 3.14

    area = PI * r * r 
    return area

def main():

    radius = int(input("Enter the radius of Circle : "))

    ret = AreaofCircle(radius)
    print("Area of Circle is : ",ret)
    
if __name__ == "__main__":
    main()