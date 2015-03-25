"""  Bismillah hir rahmanir raheem. Thanks to Allah for everything.
     Coder: Abdullah-Al-Imran
     Email: abdalimran@gmail.com  """

def Song_99():
    for i in range(99,0,-1):
        print("{} bottles of beer on the wall, {} bottles of beer.".format(i,i))
        print("Take one down, pass it around, {} bottles of beer on the wall.".format(i-1))

def Main():
    Song_99()

Main()