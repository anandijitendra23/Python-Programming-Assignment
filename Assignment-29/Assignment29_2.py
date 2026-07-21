def main():

    FileName = input("Enter name of the file : ")

    try:
        fobj = open( FileName , "r")

        for lines in fobj:
            print(lines,end="")

        fobj.close()
        
    except FileNotFoundError:
        print("File Not Found.")

if  __name__ == "__main__":
    main()
