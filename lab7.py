#write a simple decorator which adds dollar sign before the number to extend the functionality of a particular function 
def earning(x):
    print(x)
def mydec(fn):
    symbol='$'
    def wrapper(n):
        print('my earnings is '+symbol, end=' ')
        fn()
    return wrapper
earn=mydec(earning)
earn(200) 