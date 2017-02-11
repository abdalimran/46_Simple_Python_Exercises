def pangram(str):
    ss=len(set(str))
    if ss >= 26:
        return True
    else:
        return False

def Main():
    str=input()

    stripped = (''.join(ch for ch in str if ch.isalnum())).lower()

    if pangram(stripped):
        print('"{}" is a Pangram!'.format(str))
    else:
        print('"{}" is not a Pangram!'.format(str))

if __name__=="__main__":
    Main()
