def make_ing_form(w):
    if w.endswith('ie'):
        w = w.rstrip('ie')
        w +='y'+'ing'
         
    elif w.endswith('e'):
        w = w[:-1]
        w = w+'ing'
 
    elif w[-2] in 'aiou':
        w = w + w[-1] + 'ing'
 
    return w

def Main():
    w=input("Enter word:")
    print(make_ing_form(w))

if __name__=="__main__":
    Main()
