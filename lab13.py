import os 
#print(os.listdir("."))
#print(os.path.getsize('lab5.py'))
#for size in map(os.path.getsize,os.listdir('.')):
    #print(size)
'''def get(name):
    return (name,os.path.getsize(name))
for i in map(get,os.listdir('.')):
    print(i[0],'-------->',i[1])'''

#print(list(filter(lambda x:x%2==0,range(1,25))))
l=['rama','sita','lakshmana','urmila','krishna']
def fn(t):
    for i in t:
        if 'r' in i:
            return i
print(list(filter(lambda s: len(s)>4,l)))



