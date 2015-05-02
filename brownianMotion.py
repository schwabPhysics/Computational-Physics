'''This program is a depiction of brownian motion for N steps'''

#Brownian Motion
from random import uniform
from pylab import *

x = 0
y = 0
xList = [x]
yList = [y]
distance = []

N = 10000                                   #set the number of steps here
for i in range(0,N):
    dx = uniform(-1,1); dy = uniform(-1,1)  #uniform steps between -1 and 1
    x += dx; y += dy                        #take a step
    xList.append(x) 
    yList.append(y)
    distance.append(sqrt(x**2+y**2))        #all distances logged if desired


#===============plotting==================    
subplot(1,2,1)
plot(xList, yList, lw = .2)
plot(0,0, marker = '*', markersize = 15)
axhline()
axvline()
xlabel(r'$x-\mathrm{Distance}$')
ylabel(r'$y-\mathrm{Distance}$')
title(r'$\mathrm{Random\/Walk\/%i \/Steps}$' %N)
xlim(min(xList)+min(xList)/10, max(xList)+max(xList)/10)    #giving some space for the
ylim(min(yList)+min(yList)/10, max(yList)+max(yList)/10)    #picture


subplot(1,2,2)
plot([i for i in range(0,N)],distance,
     markevery = 100, marker = 'o', ls = 'none',
     mfc = 'w', label = r'$\mathrm{Position}$')
xlabel(r'$\mathrm{Number\/of\/Steps}\/N$')
ylabel(r'$\mathrm{Distance}$')
title(r'$\mathrm{Distance\/from\/Origin}$')
plot([i for i in range(0,N)], [sqrt(i) for i in range(0,N)],
     ls = '--', label = r'$\sqrt{N}$')
legend(loc='upper left')


show()
