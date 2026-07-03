def CountofDigits(no):

    if no == 0:
        count=1
    
    else:
        count = 0
        while no > 0:
            no = no // 10
            count = count + 1
    
    return count
def main():
     
    number=(int(input("Enter a number : ")))

    ret = CountofDigits(number)

    print("The number of digits are : ",ret)

if __name__ == "__main__":
    main()