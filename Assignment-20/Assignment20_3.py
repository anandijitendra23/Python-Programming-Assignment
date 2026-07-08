import threading

def EvenList(numbers):
    sum = 0

    print("Even Elements : ")
    for i in numbers:
        if i % 2 == 0:
            print(i , end = "   ")
            sum = sum + i
    print()
    print("Sum of all Even Elements is : ",sum)

def OddList(numbers):
    sum = 0

    print("Odd Elements : ")
    for i in numbers:
        if i % 2 == 1:
            print(i, end = "   ")
            sum = sum + i
    print()
    print("Sum of all Odd Elements is :",sum)

def main():

    numbers = list()

    n = int(input("Enter number of elements : "))

    for i in range(n):
        no = int(input("Enter Element : "))
        numbers.append(no)

    t1 = threading.Thread(target = EvenList , args = (numbers , ) )    
    t2 = threading.Thread(target = OddList , args = (numbers , ) )       

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from Main")

if __name__ == "__main__":
    main()