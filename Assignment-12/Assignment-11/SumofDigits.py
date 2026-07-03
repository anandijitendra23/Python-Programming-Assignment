def SumofDigits(no):
    sum = 0

    while no > 0 :
        digit = no % 10 
        sum = sum + digit
        no = no // 10

    return sum

def main():

    value = int(input("Enter a number : "))

    ret = SumofDigits(value)
    print("Sum of digits in the number is : ",ret)
    

if __name__ == "__main__":
    main()