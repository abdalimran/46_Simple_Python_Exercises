def make_3sg_form(v):
    if v.endswith('y'):
        v+='ies'
    elif v.endswith(('o','ch','s','sh','x','z')):
        v+='es'
    else:
        v+='s'
    return v

def Main():
    s=input("Enter verb:")
    print(make_3sg_form(s))

if __name__=="__main__":
    Main()
