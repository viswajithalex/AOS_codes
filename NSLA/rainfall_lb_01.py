# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 09:23:13 2025

@author: user
"""

import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cf


data =  xr.open_mfdataset("C:/Users/user/Documents/24CL05012/nsla/rainfall/*.nc")

lon = data['LONGITUDE']
lat = data['LATITUDE']
time = data['TIME']
rf = data['RAINFALL']


rf= rf.convert_calendar('noleap',dim = 'TIME')
# to remove the leap years
rf_365 = rf.groupby('TIME.dayofyear').mean(dim =('TIME'))

#%%

rf_JJAS = rf_365.isel(dayofyear = slice(151,272)).mean(dim = ('dayofyear'))

plt.figure(figsize = (12,8),dpi = 100)
ax = plt.axes(projection = ccrs.PlateCarree())
ax.coastlines()
levels = np.linspace(0,30,10)
im =  plt.contourf(lon,lat,rf_JJAS,levels,cmap = 'coolwarm_r',extend='both')
ax.add_feature(cf.LAND,color = 'grey')
# ax.add_feature(cf.BORDERS)
ax.gridlines(visible=True,draw_labels=True)
cbar = plt.colorbar(im)
cbar.set_label('Rainfall (mm)')
ax.set_title('JJAS average climatology (1991-2000)',pad= 30)

#%%

rft_JJAS =  rf_365.mean(dim = ('LONGITUDE','LATITUDE'))
plt.figure(figsize = (12,8),dpi = 100)
plt.plot(rft_JJAS)
plt.xlabel('TIME')
plt.ylabel('Rainfall (mm)')
plt.title('Time Series of Rainfall on JJAS (1991-2000)')
plt.legend()


#%%
rf_365_broadcasted = rf_365.isel(dayofyear=rf['TIME'].dt.dayofyear - 1)


rf_ano = rf - rf_365_broadcasted

rf_2000= rf_ano.sel(TIME = slice('2000-01-01','2000-12-31')).mean(dim = 'TIME')

plt.figure(figsize = (12,8),dpi = 100)
ax = plt.axes(projection = ccrs.PlateCarree())
ax.coastlines()
levels = np.linspace(-6,8,50)
im =  plt.contourf(lon,lat,rf_2000,levels,cmap = 'coolwarm_r')
ax.add_feature(cf.LAND,color = 'grey')
ax.gridlines(visible=True,draw_labels=True)
cbar = plt.colorbar(im)
cbar.set_label('Rainfall (mm)')
plt.title('Spatial Rainfall Anomaly Plot over India in 2000',pad = 40)
#%%

rf_2000_sp = rf_ano.sel(TIME = slice('2000-01-01','2000-12-31')).mean(dim = ('LATITUDE','LONGITUDE'))

plt.figure(figsize = (12,8),dpi = 100)
plt.plot(rf_2000_sp)
plt.xlabel('TIME')
plt.ylabel('Rainfall (mm)')
plt.title('Time Series of Rainfall anomaly over India in 2000')


#%%


rf_lat = 15
rf_lon = 80

rf_area = rf.sel(LATITUDE = rf_lat,LONGITUDE = rf_lon)


t = time[0:-3]

plt.figure(figsize = (12,8),dpi = 100)
plt.plot(t,rf_area)
plt.xlabel('TIME')
plt.ylabel('Rainfall (mm)')
plt.title('Time Series of Rainfall')
#%%

yf = np.fft.rfft(rf_area)

N = np.size(rf_area)

# xf = np.fft.rfftfreq(N,1)
t = np.linspace(0,3650,1826)

plt.figure(figsize= (12,4),dpi =100)
plt.plot(t,np.abs(yf))
plt.xlabel('Time')
plt.ylabel('Power')
plt.title('Power Spectra of Rainfall')
plt.grid()

#%%
ff_ano = rf_area - rf.mean(dim =('LATITUDE','LONGITUDE'))

yf1 = np.fft.rfft(ff_ano)

N1 = np.size(ff_ano)

# xf1 = np.fft.rfftfreq(N1,1)

t = np.linspace(0,3650,1826)

plt.figure(figsize= (12,4),dpi =100)
plt.plot(t,np.abs(yf1))
plt.xlabel('Time')
plt.ylabel('Power')
plt.title('Power Spectra of anomaly in daily rainfall')
plt.grid()


