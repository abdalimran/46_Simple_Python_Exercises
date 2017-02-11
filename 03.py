def length(str):

    count=0

    for c in str:
        count=count+1

    return count

def Main():

    str=input()

    print(length(str))

if __name__=="__main__":
    Main()
