def ifVowel(c):
    Vowels=['a','A','e','E','i','I','o','O','u','U']
    if c in Vowels:
        return True
    else:
        return False

def Main():
    c=input()

    if(ifVowel(c)):
        print("{} is a Vowel".format(c))
    else:
        print("{} is not a Vowel".format(c))

if __name__=="__main__":
    Main()
