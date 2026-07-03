def PerfectNumber(num):
    sum = 0

    for i in range(1,num):
        if num % i == 0:
            sum = sum + i

    return sum == num


def main():

    value = int(input("Enter a number : "))
    
    ret = PerfectNumber(value)
    
    if PerfectNumber(value):
        print("Perfect Number")
    else:
        print("Not Perfect Number")
if __name__ == "__main__":
    main()