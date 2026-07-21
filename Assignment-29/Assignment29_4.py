import sys

def main():

    File1 = sys.argv[1]
    File2 = sys.argv[2]

    fobj1 = open(File1 , "r")
    fobj2 = open(File2 , "r")

    data1 =  fobj1.read()
    data2 = fobj2.read()

    if data1 == data2:
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    main()