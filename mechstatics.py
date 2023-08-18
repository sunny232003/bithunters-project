from math import *
'''# 2/11 
# For this problem, we need to find the resultant along the x axis.
# Step 1:- resolve the 3KN force into x and y components.
import math as m
x=m.atan(4/3)
x_component_1=m.cos(x)*3000 #3KN = 3000N
y_component_1=m.sin(x)*3000
#step 2:- Resolve the 2KN force into x and y components.
x_component_2=m.cos(m.pi/6)*2000 #2KN=2000N
y_component_2=m.sin(m.pi/6)*2000
x_result= x_component_1 + x_component_2
y_result= - y_component_1 + y_component_2
result= m.sqrt(x_result**2 + y_result**2)
x_angle=360 + m.atan(y_result/x_result)*180/m.pi
print(' The magnitude of resultant R is ', result, ' and the angle it makes along the x axis is', x_angle)'''


'''#2/63
#For this problem, we need to find the couple caused by the proppellers and equate it to the couple caused by the brakes.
# couple = magnitude * the distance between the forces
couple_propeller= 2000 * 5
couple_brake=couple_propeller/ 3
print(' The force that needs to be exerted by the breaks at A and B is ', couple_brake,' newtons')'''


'''#3/10
# For this problem, we need to find the force p exerted.
# To do this, we need to equate the different forces at equilibrium
angle=asin(1/4) #at equilibrium, the opposite and hypotenuse sides are 1 and 4
tan_val=tan(angle)
horizontal_p= 50 * 9.81 * tan_val
print('The horizontal force P required to maintain the system in equilibrium is ',horizontal_p)'''


#5/47
#for this problem, we need to divide the given shape into a triangle(height a-b and breadth h) and a rectangle(height b and breadth h).
a=int(input('enter the length of the longer side of the trapezium '))
b=int(input('enter the length of the shorter side of the trapezium '))
h=int(input('enter the length of the base of the trapezium '))
ar_rect=(b)*h
ar_tri=(a-b)*h*.5
#for the centroid of rectangle:-
x_rect=b/2
y_rect=h/2
#for the centroid of triangle:-
y_tri=h/3
x_tri=b+(a-b)/3
#to find the centroid of the composite figure 
y_comp=(y_rect*ar_rect + y_tri*ar_tri)/(ar_rect+ar_tri)
x_comp=(x_rect*ar_rect + x_tri*ar_tri)/(ar_rect+ar_tri)
print('The x-coordinate of the centroid is ',x_comp,' and the y coordinate is ',y_comp)








