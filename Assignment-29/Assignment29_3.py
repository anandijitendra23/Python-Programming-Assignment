import sys

def main():
    
    SourceFile = sys.argv[1]
    Destination = sys.argv[2]
    
    fobj1 = open(SourceFile , "r")
    data = fobj1.read()

    fobj2 = open(Destination,"w")
    fobj2.write(data)

    print("File Copied Successfully.")

if __name__ == "__main__":
    main()


