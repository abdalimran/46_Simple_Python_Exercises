def is_palindrome(str):
    s=str[::-1]

    pal=False

    if str==s:
        pal=True
    else:
        pal=False

    return pal

def Main():

    str=input()

    stripped = ''.join(ch for ch in str if ch.isalnum())  #Removing all non alphanumeric letters

    if is_palindrome(stripped.lower()):
        print('"{}" is a Plindrome!'.format(str))
    else:
        print('"{}" is not a Plindrome!'.format(str))

if __name__=="__main__":
    Main()
