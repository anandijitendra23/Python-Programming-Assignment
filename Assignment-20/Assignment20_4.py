import threading

def Small(string):

    count =0

    for ch in string:
        if ch >= "a" and ch <= "z":
            count = count + 1
    
    print("TID of Small Thread is : ",threading.get_ident())
    print("Thread Name :",threading.current_thread().name)
    print("Count of Lowercase Charachters is : ",count)

def Capital(string):

    count =0

    for ch in string:
        if ch >= "A" and ch <= "Z":
            count = count + 1
    
    print("TID of Capital Thread is : ",threading.get_ident())
    print("Thread Name :",threading.current_thread().name)
    print("Count of Uppercase Charachters is : ",count)

def Digits(string):

    count = 0

    for ch in string: 
        if ch >= "0" and ch <= "9":
            count = count + 1
    
    print("TID of Digits Thread is : ",threading.get_ident())
    print("Thread Name :",threading.current_thread().name)
    print("Count of Digits is : ",count)

def main():

    string = input("Entyyer a string : ")

    t1 = threading.Thread(target = Small , args = (string ,))
    t2 = threading.Thread(target = Capital , args = (string ,))
    t3 = threading.Thread(target = Digits , args = (string ,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()

    print("Exit from Main")

if __name__ == "__main__":
    main()