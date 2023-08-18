# write a function definition for the given function header to solve the following problem 
def sq(a):
    for i in range(1,a):
        if i*i==a:
            return True
def eve(b):
    if b%2==0:
        return True
for i in range(1,25):
    if sq(i) and eve(i):
        print(i,' is both perfect square and even ')