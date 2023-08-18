cars=[{'brand':'honda','color':'silver','year':2021},{'brand':'benz','color':'black','year':2022}]
#sort it based on colour key
print(sorted(cars, key = lambda a : a['color']))