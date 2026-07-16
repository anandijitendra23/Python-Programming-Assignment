import multiprocessing
import os

def Factorial(N):
    fact = 1

    for i in range(1 , N+1):
        fact = fact * i 

    print("Process ID : ",os.getpid())
    print("Input Value : ",N)
    print("Factorial : ",fact)
    print("-----------------------------------")

    return fact



def main():
    Data = list()
    Result = list()

    Elements = int(input("Enter number of elements in the list : "))
    for i in range (Elements):
        no = int(input("Enter element :"))
        Data.append(no)

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial , Data)

    pobj.close()
    pobj.join()

    print("Resulted list is : ")
    print(Result)

if __name__ == "__main__": 
    main()
