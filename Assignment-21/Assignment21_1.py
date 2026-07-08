import threading

def Prime(numbers):

    print("Prime Numbers : ")
    
    for n in numbers:
        if n > 1:
            flag = True
            for i in range(2,n):
                if n % i == 0:
                    flag = False
                    break
            
            if flag:
                print(n,end = "  ")
    print()

def NonPrime(numbers):

    print(" Non Prime Numbers : ")
    
    for n in numbers:
        if n <= 1:
            print(n,end = "  ")
        else:
            flag = False
            for i in range(2,n):
                if n % i == 0:
                    flag = True
                    break
            
            if flag:
                print(n,end = "  ")
    print()    

def main():

    numbers = list()

    n = int(input("Enter number of elements : "))
    for i in range(n):
        n = int(input("Enter element : "))
        numbers.append(n)

    t1 = threading.Thread(target = Prime , args = (numbers ,))
    t2 = threading.Thread(target = NonPrime , args = (numbers ,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from Main ")

if __name__ == "__main__":
    main()