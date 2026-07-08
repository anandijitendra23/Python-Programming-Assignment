import threading

def Thread1():
    print("Numbers from 1 to 50 : ")

    for i in range(1,51):
          print(i , end = "  ")
    print()

def Thread2():
    print("Numbers from 1 to 50 in Reverse Order : ")
    for i in range(50 , 0 ,-1):
        print(i,end = "  ")
    print()

def main():
     
    t1 = threading.Thread(target = Thread1)
    t2 = threading.Thread(target = Thread2)

    t1.start()
    t1.join()
    
    t2.start()
    t2.join()

    print("Exit from Main")
if __name__ == "__main__":
    main()