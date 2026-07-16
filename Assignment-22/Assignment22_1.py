import multiprocessing

def SumSquare(Num):
    Sum = 0

    for i in range (1,Num+1):
        Sum = Sum + (i * i)
    return Sum

def main():

    Data = []
    Result = []

    n = int(input("Enter number of elements : "))
    for i in range (n):
        no = int(input("Enter element : "))
        Data.append(no)

    
    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquare , Data)

    pobj.close()
    pobj.join()

    print("Result is : ")
    print(Result)

if __name__ == "__main__":
    main()