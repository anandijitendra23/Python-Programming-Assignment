import threading

def main():

    Count = [10000]
    Lock = threading.Lock()

    print(Count)

    t1 = threading.Thread(target = Function , args = (Count , Lock))
    t2 = threading.Thread(target = Function , args = (Count , Lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

def Function(Count , Lock):
    
    Lock.acquire()
    Count[0] = Count[0] + 10000
    Lock.release()

    print(Count)

if __name__ == "__main__":
    main()
