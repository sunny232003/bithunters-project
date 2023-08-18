d={'apple':'fruit','banana':'fruit','cat':'animal','dog':'animal'}
def uniq(d1):
    n={}
    for key in d1:
        val=d1[key]
        if val not in n:
            n[val]=[]
        n[val].append(key)
    return n

print(uniq(d))
