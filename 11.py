def generate_n_chars(n,c):
    s=""
    for i in range(0,n):
        s+=c
    return s


def Main():
    n=int(input())
    c=input()

    print(generate_n_chars(n,c))

if __name__=="__main__":
    Main()
