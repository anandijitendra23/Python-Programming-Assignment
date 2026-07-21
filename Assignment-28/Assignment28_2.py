def main():

    FileName = input("Enter the File Name : ")
    fobj = open(FileName , "r")

    count = 0
    for line in fobj :
        word = line.split()
        count = count + len(word)
    
    fobj.close()

    print(f"Total number of words in {FileName} are : ",count)

if __name__ == "__main__":
    main()