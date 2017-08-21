# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

from mpl_toolkits.basemap import Basemap,maskoceans
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
    
llcrnrlat=43
llcrnrlon=-116
urcrnrlat=50
urcrnrlon=-103
cobertura=0.2
m=Basemap(projection='mill',llcrnrlat=llcrnrlat,llcrnrlon=llcrnrlon,urcrnrlat=urcrnrlat,urcrnrlon=urcrnrlon,resolution='c')
x_min,y_min=m(llcrnrlon,llcrnrlat)
x_max,y_max=m(urcrnrlon,urcrnrlat)

#numero de datos ficticios (prueba)
n=1000

#longitud de los cuadrados de la grilla en grados
l=1

#dimensiones de la grilla
height=urcrnrlat-llcrnrlat
length=urcrnrlon-llcrnrlon
"""
tweets_array=np.array([np.random.uniform(low=llcrnrlat,high=height+llcrnrlat,size=n),
                       np.random.uniform(low=llcrnrlon,high=length+llcrnrlon,size=n),
                       np.random.binomial(np.ones(n).astype(int),np.ones(n)*0.5)]).transpose()
tweets=pd.DataFrame(tweets_array,columns=['lat','lon','clase'])
"""
tweets=pd.read_csv("cebo_final.tsv",sep="\t",names=['clase','lat','lon'])

tweets=tweets.iloc[np.where(tweets['lat']>=llcrnrlat)]
tweets=tweets.iloc[np.where(tweets['lon']>=llcrnrlon)]
tweets=tweets.iloc[np.where(tweets['lat']<=urcrnrlat)]
tweets=tweets.iloc[np.where(tweets['lon']<=urcrnrlon)]
tweets.reset_index(inplace=True)
#una región se define por las coordenadas de su centro
ceros=np.where(tweets['clase']==0)[0]
tweets['clase'][np.where(tweets['clase']==2)[0]]=0
tweets['clase'][np.where(tweets['clase']==1)[0]]=1.1
tweets['clase'][ceros]=3.5
tweets[['lat','lon']]=tweets[['lat','lon']]-(tweets[['lat','lon']]%l)
regiones=tweets.groupby(['lat','lon']).agg(['sum','count']).clase
regiones['x'],regiones['y']=m(np.array(regiones.index.get_level_values('lon')),np.array(regiones.index.get_level_values('lat')))
#tweets['x'],tweets['y']=m(tweets['lon'],tweets['lat'])
regiones['avg']=regiones['sum']/regiones['count']

#ratio=(x_max-x_min)/(y_max-y_min)
#nbins=30
#heatmap, xedges, yedges = np.histogram2d(regiones['x'], regiones['y'],bins=[int(nbins*ratio),nbins],weights=regiones['avg'], range=[[x_min,x_max],[y_min,y_max]])
#heatmap, xedges, yedges = np.histogram2d(tweets['x'], tweets['y'],bins=[int(nbins*ratio),nbins],weights=tweets['clase'], range=[[x_min,x_max],[y_min,y_max]])
extent = [x_min, x_max, y_min, y_max]

M=np.zeros(((int((urcrnrlat-llcrnrlat)/l)),(int((urcrnrlon-llcrnrlon)/l))))
for i in range(regiones.shape[0]):
    coords=regiones.iloc[i].name
    try:
        M[int((coords[0]-llcrnrlat)/l),int((coords[1]-llcrnrlon)/l)+1]=regiones.iloc[i].avg
    except: pass

#plt.imshow(heatmap.T,interpolation='bicubic',extent=extent,cmap='coolwarm',origin='lower')
plt.imshow(M,interpolation='bicubic',extent=extent,cmap='coolwarm',origin='lower')
m.drawcountries()
m.drawcoastlines()
m.drawstates()
plt.colorbar(orientation='horizontal',shrink=0.9)
plt.savefig('testplot1.png',dpi=900)
plt.show()

hotspots=regiones[['avg']].sort_values(by='avg',ascending=False).iloc[range(int(regiones.shape[0]*0.2))]
hotspots['lat']=hotspots.index.get_level_values('lat')
hotspots['lon']=hotspots.index.get_level_values('lon')