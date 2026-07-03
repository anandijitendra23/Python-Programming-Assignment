def VowelorConsonent(ch):

    if (ch == 'A' or ch == 'E'or ch == 'I'or ch == 'O' or ch == 'U' or 
        ch == 'a' or ch == 'e'or ch == 'i'or ch == 'o' or ch == 'u' ):
        return True
    else:
        return False

def main():

    char = input("Enter a alphabet : ")

    ret = VowelorConsonent(char)

    if VowelorConsonent(char):
        print("Vowel")
    else:
        print("Consonant")


if __name__ == "__main__":
    main()