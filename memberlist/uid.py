from string import strip

def getuid():
    _list = []
    t = open('memberlist/uid.txt').readlines()
    l = map(strip, t)
    #_l = map(split(' '), map(,l))
    #_l = l[0].split(' ')
    for x in l:
        _list.append(x.split(' '))
    return _list
    
