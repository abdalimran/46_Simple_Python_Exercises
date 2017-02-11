def ifConsonant(c):
    Vowels=['a','A','e','E','i','I','o','O','u','U']
    if c not in Vowels:
        return True
    else:
        return False

def translate(str):

    tString=""

    for c in str:
        if(ifConsonant(c) and (c !=" ")):
            tString+=c+"o"+c
        else:
            tString+=c

    return tString

def Main():

    str=input()

    print(translate(str))

if __name__=="__main__":
    Main()
