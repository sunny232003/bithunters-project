#Question 1 2/6


import pandas as pd 
import numpy as np
import math 



rad = int(input("Enter the radius of the semi-circle in m"))
base = int(input("Enter the base of the triangle in m ")) 
height = int(input("Enter the height of the triangle")) 
moi_sc = (0.25 * 3.141 * rad**4) 
moi_tr_x =-1*((1/12)*base*height**3) 
moi_tr_y = -1*((2/12)*((base/2)**3)*height) 
moi_tr_z = moi_tr_x + moi_tr_y
total_moi = moi_sc - moi_tr_z 
print(total_moi)
