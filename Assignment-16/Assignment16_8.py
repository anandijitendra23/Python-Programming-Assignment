def Star(no):
    for i in range(no ):
        print("*",end = "    ")

def main():
    
    num = int(input("Enter a number : "))

    Star(num)

if __name__ == "__main__":
    main()