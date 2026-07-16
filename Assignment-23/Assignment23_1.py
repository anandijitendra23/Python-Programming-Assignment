import multiprocessing
import os

def SumEven(N):
    Sum = 0

    for i in range (1 , N+1):
        if i % 2 == 0:
            Sum = Sum + i

    print("Process ID : ",os.getpid())
    print("Input Value : ",N)
    print("Sum of Even Numbers : ",Sum)
    print("-----------------------------------")

    return Sum


def main():
    Data = list()
    Result = list()

    Elements = int(input("Enter number of elements in the list : "))
    for i in range (Elements):
        no = int(input("Enter element :"))
        Data.append(no)

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumEven , Data)

    pobj.close()
    pobj.join()

    print("Resulted list is : ")
    print(Result)

if __name__ == "__main__":
    main()
