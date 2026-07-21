import os

def main():
    FileName = input("Enter the name of  the file : ")

    ret = os.path.exists(FileName)

    if ret == True :
        print(FileName ,"file exists.")

    else:
        print(FileName,"does not exist.")

if __name__ == "__main__":
    main()