import multiprocessing

def IsPrime(N):
    if N < 2 :
        return False
    
    for i in range(2,N+1):
        if N % i == 0:
            return False
    
    return True

def CountPrime(no):
    count = 0
    for i in range(1,no+1):
        if IsPrime(i):
            count = count + 1

    return count

def main():
    Data = []
    Result = []

    n = int(input("Enter number of elements : "))
    for i in range (n):
        no = int(input("Enter element : "))
        Data.append(no)

    pobj = multiprocessing.Pool()

    Result = pobj.map(CountPrime , Data)

    pobj.close()
    pobj.join()

    for i in range(len(Data)):
        print("Prime numbers between 1 and ",Data[i],"=",Result[i])

if __name__ == "__main__":
    main()


