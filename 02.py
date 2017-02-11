def max_of_three(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z


def Main():
    x,y,z=input().split()
    x=input(x)
    y=input(y)
    z=input(z)

    print(max_of_three(x,y,z))

if __name__=="__main__":
    Main()
