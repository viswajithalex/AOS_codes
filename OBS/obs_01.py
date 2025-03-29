# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 17:43:17 2025

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt


file  = np.genfromtxt('C:/Users/user/Desktop/data.txt')


depth = file[0:188,1]
temp = file[0:188,2]
temp2 = file[0:188,3]
sal = file[0:188,6]
sal2 = file[0:188,7]

mask1 = -9.99e-29

#masking -9.99e-29 value from numpy array

depth = depth[depth!= mask1]
sal = sal[sal!= mask1]
sal2 = sal2[sal2!= mask1]
temp = temp[temp!= mask1]
temp2 = temp2[temp2!= mask1]


#%%plotting 

fig, ax1 = plt.subplots(figsize =(12,8),dpi =100)
plt.gca().invert_yaxis()
ax1.plot(temp,depth,color = 'red')
ax1.set_xlabel('Temperature ($^\circ$C)')
ax1.set_ylabel('Depth (m)')
ax1.tick_params(axis = 'x' ,labelcolor = 'red')

ax2 = ax1.twiny()
ax2.plot(sal,depth,color = 'blue')
ax2.set_xlabel('Salinity (PSU)',pad = 30)
ax2.tick_params(axis = 'x' ,labelcolor = 'blue')