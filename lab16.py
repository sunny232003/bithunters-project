l1=['walk','sleep','talk','eat']
def mymap(f,l):
    l1=[]
    for i in l:
        a=f[l]
        l1.append(a)
    print(l1)
mymap(lambda x: x+'ing',l1)    