def Max(x,y):
    if x>y:
        return x
    else:
        return y

def Main():
    x=int(input())
    y=int(input())

    print(Max(x,y))

if __name__=="__main__":
    Main()
