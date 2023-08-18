#l=['rama','sita','lakshmana','urmila','krishna']
#print(list(filter(lambda s:len(s)>4,map(str.upper,l))))
#l=['b sections','103','room number','1st hour','python']
#print(list(filter(lambda s: s[0].isdigit() is False,l)))
#print(sum(range(1,10)))
import functools as fn
#print(fn.reduce(lambda x,y: x+y,range(1,11),100))
#l=['raja','ram','mohan','roy']
#print(fn.reduce(lambda x,y: x+y,l))
l=['chitra','g','m']
print(fn.reduce(lambda x,y:x+y[0],l,''))