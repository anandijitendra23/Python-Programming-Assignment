import os
import multiprocessing
import time

def Power(n):
    sum = 0

    for i in range (1,n+1):
        sum = sum + i ** 5

    return sum

def main():
    Data = []
    Result = []

    n = int(input("Enter number of elements : "))
    for i in range (n):
        no = int(input("Enter element : "))
        Data.append(no)

    start_time = time.perf_counter()
    
    pobj = multiprocessing.Pool()

    Result = pobj.map(Power , Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result list is : ")
    print(Result)

if __name__ == "__main__":
    main()
