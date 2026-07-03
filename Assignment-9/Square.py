def Square(no):
    res=no*no
    return res

def main():
    value=int(input("Enetr a number : "))
    
    ret=Square(value)
    print("Square of the given number is : ",ret)

if __name__ == "__main__":
    main()