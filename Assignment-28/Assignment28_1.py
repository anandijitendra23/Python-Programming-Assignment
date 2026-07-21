def main():

    FileName = input("Enter the File Name : ")
    fobj = open(FileName , "r")

    count = 0
    for lines in fobj :
        count = count + 1
    
    fobj.close()

    print(f"Total number of lines in {FileName} are : ",count)

if __name__ == "__main__":
    main()