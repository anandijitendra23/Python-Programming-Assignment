import os
import multiprocessing

def Factorial(n):
    fact = 1

    for i in range (1 , n + 1):
        fact = fact * i

    print("Process ID : ",os.getpid())
    print("Input value : ",n)
    print("Factorial is : ",fact)
    print("------------------------------------")

    return fact

def main():

    Data = []
    Result = []

    n = int(input("Enter number of elements : "))
    for i in range (n):
        no = int(input("Enter element : "))
        Data.append(no)

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial , Data)

    pobj.close()
    pobj.join()

    print("Reasult list is : ")
    print(Result)

if __name__ == "__main__":
    main()