'''remove the tuple where 2nd number is not a factor of first
l=[(2,5),(6,3),(4,2),(10,3)]
print(list(filter(lambda s :s[0]%s[1]==0,l)))'''
 '''write a function to mimic reduce called my reduce. test this function with the following calls.
 1) find the maximum in the list
 2) given a list of integers, combine all of them to form a single integer'''
'''l=[11,1,22,2,33,3,100]
def myreduce(f,l):
    r=l[0]
    for i in l[1:]:
        r=f(r,i)
    return r
print(myreduce(lambda x,y: x if x>y else y,l))
print(f(lambda x,y: int(str(x)+str(y)),l))'''

#waf mymap which takes a callable and an iterable, creates a list, applies the callable to each element of the iterable and puts the result into the list and returns it
#1) append ing to the iterables elements
#2) return a list of tuple of the word and its length

l1=['walk','sleep','talk','eat']
def mymap(f,l):
    l1=[]
    for i in l:
        a=f[l]
        l1.append(a)
    print(l1)
mymap(lambda x: x+'ing',l)