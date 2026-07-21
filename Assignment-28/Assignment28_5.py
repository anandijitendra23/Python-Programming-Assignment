def main():

    FileName = input("Enter the File Name : ")
    fobj = open(FileName , "r")

    SearchWord = input("Enter the word to search : ")

    found = False

    for line in fobj :
        words = line.split()

        if SearchWord in words:
            found = True
            break

    fobj.close()

    if found:
        print(f"Word {SearchWord} is present in {FileName}.")
    else:
        print(f"{SearchWord} is not present in {FileName}")
    
if __name__ == "__main__":
    main()