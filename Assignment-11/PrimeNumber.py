def Prime(no):
            
    if no <= 1:
        return False
    
    for i in range(2,no):
        if no % i == 0:
            return False
        
    return True
def main():

    value = int(input("Enter a number : "))

    if Prime(value):
        print("Prime Number")
    
    else:
        print("Not Prime Number")


if __name__ == "__main__":
    main()