import multiprocessing
import os

def CountOdd(N):
    Count = 0

    for i in range (1 , N+1):
        if i % 2 != 0:
            Count = Count + 1

    print("Process ID : ",os.getpid())
    print("Input Value : ",N)
    print("Odd Number Count : ",Count)
    print("-----------------------------------")

    return Count


def main():
    Data = list()
    Result = list()

    Elements = int(input("Enter number of elements in the list : "))
    for i in range (Elements):
        no = int(input("Enter element :"))
        Data.append(no)

    pobj = multiprocessing.Pool()

    Result = pobj.map(CountOdd , Data)

    pobj.close()
    pobj.join()

    print("Resulted list is : ")
    print(Result)

if __name__ == "__main__": 
    main()
