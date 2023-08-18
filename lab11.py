l=['lmao','lol','yes']
def f(g):
    res=[]
    for i in g:
        res.append(i)
    return res
k=f(l)
#print(k)

print(list(map(len,l)))