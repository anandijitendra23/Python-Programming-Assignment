import threading

sum = 0
prod = 1

def Sum(numbers):
    global sum

    for n in numbers : 
        sum = sum + n 

def Product(numbers):
    global prod

    for n in numbers:
        prod = prod * n

def main():

    numbers = list()

    n = int(input("Enter number of elements : "))
    for i in range(n):
        n = int(input("Enter element : "))
        numbers.append(n)

    t1 = threading.Thread(target = Sum , args = (numbers ,))
    t2 = threading.Thread(target = Product , args = (numbers ,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements is : ",sum)
    print("Product of elements is : ",prod)

    print("Exit from Main ")

if __name__ == "__main__":
    main()