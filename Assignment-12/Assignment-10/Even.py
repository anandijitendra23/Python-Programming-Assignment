def Even(no):

    result = []

    for i in range(1,no+1):
        if i % 2 == 0:
            result.append(i)
            
    return result
        

def main():

    value = int(input("Enter a number : "))

    ret = Even(value)
    print("Even numbers are : ",ret)

if __name__ == "__main__":
    main()