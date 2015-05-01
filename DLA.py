#This program takes a single seed centered at the origin and releases a randomly walking particle. If 
#the particle comes within a specified range of the seed, then it will stop walking. Subsequently, 
#another particle will be sent walking randomly until it sticks to the cluster. The resulting image
#is the product of Diffusion-limited aggregation. This can be seen as general crystal growth





#Diffusion-limited aggregation
from math import *
from pylab import *
from random import randint

'''this function takes the radius of the furthest
sticking point and returns a starting point for
the next particle'''
def drop_a_point(r):
    xcircle = (r*1.1)*cos(arange(0,100))
    ycircle = (r*1.1)*sin(arange(0,100))
    c = randint(0,99)
    xStart = xcircle[c]
    yStart = ycircle[c]
    return (xStart, yStart)

'''This function takes a particular spot x,y and checks
to see if it is within range of any seeds. If it is, then
it will return the bool stick as true. If not, then stick 
remains false'''
def sticky_spot(x,y,listOfSeeds, stick):
    X=0;Y=0
    for seed in listOfSeeds:
        if ((seed[0]-x)**2+(seed[1]-y)**2) <= .5:
            stick = True
            X = seed[0]; Y = seed[1]
    return stick, X, Y

'''The most important function here is how the particles walk.
the particle starts off on a spot along a circle defined by start, 
which is created from the earlier function. Then, the particle walks
in a random 2d direction. If the particle gets too far away, we reset
the particle and try again until it sticks. At which point, the function 
returns where the particle stuck, and to which seed it stuck to. '''
def walk_to_stick(listOfSeeds, start, r):
    x = start[0]
    y = start[1]
    stick = False
    while stick == False:
        c = randint(-1,1)
        d = randint(-1,1)
        x += c
        y += d
        stick, seedX, seedY = sticky_spot(x,y,listOfSeeds, stick)
        #print 'missed'
        if (x**2 + y**2 > 2*r**2):
            x = start[0]
            y = start[1]
            #print 'restarted'
    return (x,y), seedX, seedY

#====================================================================
xLimits = range(-30,31)
ylimits = range(-30,31)

#set the seed
x0 = 0
y0 = 0
listOfSeeds = [(0,0)]


r = 1
count = 0
N = 500
for i in range(0,N):
    start = drop_a_point(r)
    stickyPoint, seedX, seedY = walk_to_stick(listOfSeeds, start, r)
    listOfSeeds.append(stickyPoint)
    plot([stickyPoint[0], seedX],[stickyPoint[1], seedY],'b', lw = 1)
    if (stickyPoint[0]**2+stickyPoint[1]**2>r**2):
        r = sqrt(stickyPoint[0]**2+stickyPoint[1]**2)
    count += 1
    if count%10 == 0:
        print count
    
axhline(linestyle = '--')
axvline(linestyle = '--')
title(r'$\mathrm{Diffussion-limited\/Aggregation\/for\/ %i \/particles}$' %N)

show()
