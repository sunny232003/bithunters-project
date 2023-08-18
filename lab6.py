#waf to get a matrix
def ide(x):
    for i in range(1,x+1):
        for j in range(1,x+1):
            if i==j:
                print(1,end=' ')
            else:
                print(0,end=' ')
        print()
ide(3)