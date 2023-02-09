# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 00:42:06 2023

@author: ARKAJYOTI GUCHHAIT
"""

import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os
from math import sqrt
from copy import deepcopy

filenames=[]
t=0
it=0
dt=0.0628

while it<=100:
    def makefield(xs,ys):
        postoq={(-1,0):1, (1,0):1, (2*np.cos(t),2*np.sin(2*t)):-2}
        n=len(xs)
        Exs=[[0 for k in range(n)] for j in range(n)]
        Eys=deepcopy(Exs)
        for j,x in enumerate(xs):
            for k,y in enumerate(ys):
                for pos,q in postoq.items():
                    posx,posy=pos
                    R=sqrt((x-posx)**2+(y-posy)**2)
                    Exs[k][j]+= q*(x-posx)/R**3
                    Eys[k][j]+= q*(y-posy)/R**3
        return Exs, Eys
    
    def plotfield(boxl,n):
        xs=[-boxl+i*2*boxl/(n-1) for i in range(n)]
        ys=xs[:]
        Exs,Eys=makefield(xs,ys)
        xs=np.array(xs); ys=np.array(ys)
        Exs=np.array(Exs); Eys=np.array(Eys)
        plt.streamplot(xs,ys,Exs,Eys, density=2, color='r',linewidth=0.5, arrowstyle='->')
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        filename='_tmp_'+str(it).zfill(5)+'.png'
        filenames.append(filename)
        plt.savefig(filename)
        plt.show()
    plotfield(2.5,20)
   
    
    plt.close()
    t=t+dt
    it=it+1

print(filenames)

with imageio.get_writer('animated2.gif',mode='I') as writer:
    for filename in filenames:
        image=imageio.imread(filename)
        writer.append_data(image)
        
for filename in set(filenames):
    os.remove(filename)
                    
        