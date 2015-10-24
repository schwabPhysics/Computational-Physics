'''This is an old file of mine that I plan on reworking for effeciency and clarity. Currently though, it 
has some interesting points in it about the 'correct' answer to bertand's paradox'''

from pylab import *
from math import *
from numpy import arange, sin, cos, pi, linspace, sqrt
from random import randint

#make a large circle
t = linspace(0,2*pi,1000)
X = cos(t)
Y = sin(t)

#x and y values for later
modX = linspace(-1,1,1000)
modY = linspace(-1,1,1000)


#a function that takes a midpoint and returns the points on the circle
def points_on_circle(xm,ym):
    x=xm; y=ym
    while x**2 + y**2<1:
        x += -ym*0.01
        y += xm*0.01
    x1 = x; y1 = y
    x = xm; y = ym
    while x**2 + y**2<1:
        x -= -ym*0.01
        y -= xm*0.01
    x2 = x; y2 = y
    return x1, x2, y1, y2

#a function that takes a point (midpoint) and returns the value on the axis
#which it intersects. This is used for the broomstick method
def find_the_line(x,y,slope):
    b = y+1/slope*x
    newx = b/(slope+1/slope)
    newy = -b/slope/(slope+1/slope)+b
    return newx, newy


#-----------------------Distribution of Midpoints--------------------
#chord center distribution from smaller circles for midpoint theory corrected
chord_center = []
figure(2, figsize=(15,8))
subplot(2,3,5)
plot(X,Y)
title(r'$\mathrm{Midpoint\/Corrected}$')
midx = []
for i in range(0,len(X),20):
    x = .5*cos(t)+X[i]/2
    y = .5*sin(t)+Y[i]/2
    for i in range(0,len(x)):
        chord_center.append((x[i],y[i]))
    plot(x,y,'.k', lw = .5, markevery = 100)
xlim(-1.1,1.1)
ylim(-1.1,1.1)

print 'done with midpoint distribution'

#chord center distribution for midpoint (wrong)
figure(2)
subplot(2,3,2)
plot(X,Y)
title(r'$\mathrm{Picking\/Midpoints\/Wrong} $')
for i in range(0, len(modX),50):
    for j in range(0, len(modY), 50):
        if modX[i]**2 + modY[j]**2 <=1:
            plot(modX[i], modY[j], 'k.')
xlim(-1.1,1.1)
ylim(-1.1,1.1)

#chord center distribution for 'right' method
figure(2)
subplot(2,3,1)
plot(X,Y)
title(r'$\mathrm{Chord\/Center\/Distribution\/True}$')
x = .5*cos(t)+X[0]/2
y = .5*sin(t)+Y[0]/2
plot(x,y, 'k.', markevery = 50, lw = .5)
xlim(-1.1,1.1)
ylim(-1.1,1.1)

print 'done with right midpoint distribution'

#putting lines through previous
figure(2)
subplot(2,3,4)
plot(X,Y)
title(r'$\mathrm{Lines\/To\/Edges}$')
plot(x,y, 'k.', markevery = 50, lw = .5)
for i in range(0, len(x), 50):
    x1, x2, y1, y2 = points_on_circle(x[i], y[i])
    plot((x1, x2), (y1, y2), 'k', lw = .5)
xlim(-1.1,1.1)
ylim(-1.1,1.1)

#chord center distribution for broomstick
figure(2)
subplot(2,3,3)
plot(X,Y)
title(r'$\mathrm{Chord\/Center\/Distribution\/Broomstick} $')
x = []
for item in modY:
    x.append(0)
plot(x,modY, 'k.', lw = .5, markevery = 50)
xlim(-1.1,1.1)
ylim(-1.1,1.1)

print 'done with broomstick centers'

#corrected broomstick
figure(2)
subplot(2,3,6)
plot(X,Y)
title(r'$\mathrm{Broomstick\/Corrected} $')
x = []
y = []
for i in range(0, len(Y)):
    y.append(Y[i])
    x.append(0)
plot(x,y, 'k.', lw = .5, markevery = 10)
xlim(-1.1,1.1)
ylim(-1.1,1.1)

print 'done with corrected broomstick'


#---------------------Random Chords-------------------------
N = 500

#draw random chords from random points on large circle
figure(1, figsize=(15,8))
suptitle(r'$\mathrm{Different\/ways\/to\/pick\/%s\/Pseudo\/Random\/Chords}$' %str(N), fontsize = 'x-large')
subplot(2,3,1)
plot(X,Y)
title(r'$\mathrm{Pairs\/on\/Circle}$')
Sum = 0
count = 0
for i in range(N):                                                      #this loop goes through the 1000 points on the
    a = randint(0, len(X)-1)                                            #circle and picks two points to connect to make
    b = randint(0, len(Y)-1)                                            #the chord
    tup1 = (X[a],X[b])
    tup2 = (Y[a],Y[b])
    plot(tup1, tup2, lw = .5, color = 'black')
    Sum += sqrt((abs(X[a]-X[b]))**2+(abs(Y[a]-Y[b]))**2)                #here is the length of the chord
    if sqrt((abs(X[a]-X[b]))**2+(abs(Y[a]-Y[b]))**2) > sqrt(3):         #and then counting if it is larger than side of
        count += 1                                                      #the triangle
        
print
print 'average distance from center for pairs method is %.2f radii' %(float(Sum)/N)
print '"prob" of success for pairs method is %.2f' %(float(count)/N)
print

xlim(-1.1,1.1)
ylim(-1.1,1.1)

print 'done with %s pairs' %str(N)
print

#random chords from random points inside the circle (wrong midpoint)
figure(1)
subplot(2,3,3)
plot(X,Y)
title(r'$\mathrm{Chord\/Centers\/Wrong}$')
list_of_points =[]
for x in modX:                                                          #this loop makes a list of points that are equally
    for y in modY:                                                      #spaced in the region of the circle
        if x**2 + y**2 <= 1:
            list_of_points.append((x,y))
Sum = 0
count = 0
chordList1 = []
littler1 = 0
for i in range(N):                                                      #here, we are picking the random chords
    c = randint(0,len(list_of_points)-1)                                #by picking a midpoint out of the list and calling
    xm = list_of_points[c][0]                                           #the points_on_circle function to find where
    ym = list_of_points[c][1]                                           #that line intersects the circle
    littler1+=sqrt(xm**2+ym**2)
    x1, x2, y1, y2 = points_on_circle(xm, ym)
    plot((x1,x2),(y1,y2), lw = 0.5, color = 'black')
    Sum+=sqrt((abs(x1-x2))**2+(abs(y1-y2))**2)
    chordList1.append(round(sqrt((abs(x1-x2))**2+(abs(y1-y2))**2),4))
    if sqrt((abs(x1-x2))**2+(abs(y1-y2))**2) > sqrt(3):
        count += 1
xlim(-1.1,1.1)
ylim(-1.1,1.1)
print 'average distance from center for "wrong" midpoint method is %.2f radii' %(float(Sum)/N)
print '"prob" of success for wrong midpoint is %.2f' %(float(count)/N)
print 'average midpoint distance is %.2f radii' %(float(littler1)/N)
print
print
    
print'done with %s random midpoints'%str(N)
print

#midpoint corrected
figure(1)
subplot(2,3,6)
plot(X,Y)
title(r'$\mathrm{Chord\/Centers\/Corrected}$')
chord_center = []
chordList2 = []
littler2 = 0
for i in range(0,len(X)):                                               #this is the proper number and distribution of
    x = .5*cos(t)+X[i]/2                                                #midpoints in the circle. This can be visualized
    y = .5*sin(t)+Y[i]/2                                                #by taking a smaller circle of radius 1/2R and 
    for i in range(0,len(x)):                                           #rotating it in the larger circle
        chord_center.append((x[i],y[i]))
Sum = 0
count = 0
for i in range(N):
    c = randint(0,len(chord_center)-1)
    littler2+=sqrt(chord_center[c][0]**2+chord_center[c][1]**2)
    x1, x2, y1, y2 = points_on_circle(chord_center[c][0], chord_center[c][1])
    plot((x1, x2), (y1, y2), lw = 0.5, c = 'black')                     #this is the same method as before, but with
    Sum+=sqrt((abs(x1-x2))**2+(abs(y1-y2))**2)                          #different midpoints (right ones)
    chordList2.append(round(sqrt((abs(x1-x2))**2+(abs(y1-y2))**2),4))
    if sqrt((abs(x1-x2))**2+(abs(y1-y2))**2) > sqrt(3):
        count += 1
xlim(-1.1,1.1)
ylim(-1.1,1.1)
print 'average distance from center for right midpoint method is %.2f radii' %(float(Sum)/N)
print '"prob" of success for right midpoint is %.2f' %(float(count)/N)
print 'average midpoint distance is %.2f radii' %(float(littler2)/N)
print

print 'done with %s midpoints corrected'%str(N)
print

#broomstick wrong
figure(1)
subplot(2,3,2)
plot(X,Y)
Sum = 0
count = 0
for i in range(N):                                                      #this loop picks 'random' chords by choosing
    a = randint(0, len(X)-1)                                            #a single point along the axis of the first
    tup1 = (X[a],Y[a])                                                  #point chosen. So pick a point, draw a line
    xpoints = linspace(X[a], -X[a], 500)                                #that is perpendicular to the circle at that
    ypoints = linspace(Y[a], -Y[a], 500)                                #spot, then pick a point on that line
    b = randint(1, len(xpoints)-1)                                      #but notice the points we are choosing from are
    xwrong = xpoints[b]                                                 #equally spaced from one side of the circle to 
    ywrong = ypoints[b]                                                 #the other
    x1, x2, y1, y2 = points_on_circle(xwrong, ywrong)
    plot((x1,x2),(y1,y2), 'black', lw = .5)
    Sum+=sqrt((abs(x1-x2))**2+(abs(y1-y2))**2)
    if sqrt((abs(x1-x2))**2+(abs(y1-y2))**2) > sqrt(3):
        count += 1
xlim(-1.1,1.1)
ylim(-1.1,1.1)
title(r'$\mathrm{Rotating\/Broomstick\/Wrong}$')
print 'average distance from center for "wrong" broomstick method is %.2f radii' %(Sum/N)
print '"prob" of wrong broomstick is %.2f' %(float(count)/N)
print


axes((.53, .54, .1, .19))
plot(X,Y)
#title(r'$\mathrm{500\/Broomstick}$')
for i in range(N):                                                      #this is essentially a simplified version of
    c = randint(0, len(modY)-1)                                         #the above method. Instead of choosing a 
    y = modY[c]                                                         #random first point, we stick with one and 
    x = sqrt(1-y**2)                                                    #draw chords along the axis of that point
    plot((x, -x), (y, y), lw = 0.5, color = 'black')                    #notice, again, that the points to choose
xlim(-1.1,1.1)                                                          #from are in the mod list - so equally spaced
ylim(-1.1,1.1)
tick_params(labelbottom='off',
            bottom='off',
            labelleft='off',
            top='off',
            right='off',
            left='off')

print 'done with %s wrong broomstick'%str(N)
print
        
#random chords from the broomstick corrected
figure(1)
subplot(2,3,5)
plot(X,Y)
Sum=0
count = 0
for i in range(N):                                                      #this loop chooses chords by first picking a
    c = randint(0, len(X)-1)                                            #random spot on the circle, then drawing the 
    tup2 = (X[c], Y[c])                                                 #perpendicular axis. But instead of choosing
    slope = (Y[c])/(X[c])                                               #our second point from evenly spaced points
    d = randint(0,len(X)-1)                                             #we are choosing from the points on the circle
    newx, newy = find_the_line(X[d],Y[d], slope)                        #this way, we have the proper distribution of
    x1, x2, y1, y2 = points_on_circle(newx, newy)                       #points to choose from in drawing the chord
    plot((x1, x2),(y1,y2), 'black', lw = .5)
    Sum += sqrt((abs(x1-x2))**2+(abs(y1-y2))**2)
    if sqrt((abs(x1-x2))**2+(abs(y1-y2))**2) > sqrt(3):
        count += 1
xlim(-1.1,1.1)
ylim(-1.1,1.1)
title(r'$\mathrm{Rotating\/Broomstick\/Corrected}$')
print 'average distance from center for right broomstick is %.2f radii' %(float(Sum)/N)
print '"prob" for right broomstick is %.2f' %(float(count)/N)
print


axes((.53,.1,.1,.19))
plot(X,Y)
#title(r'$\mathrm{500\/Random\/Broomstick\/Corrected}$')
left_side_points = []
for i in range(0, len(X)-1):
    if X[i]<=0:
        left_side_points.append((X[i],Y[i]))

for i in range(N):                                                      #like before, this is another simplified version
    c = randint(0, len(left_side_points)-1)                             #of the above method. We have stuck with one
    x1 = left_side_points[c][0]                                         #initial position and rolled the stick over the 
    y1 = left_side_points[c][1]                                         #circle, but have choosen the right distribution
    plot((x1,-x1), (y1, y1), lw = 0.4, color = 'black')                 #for the points to choose from
xlim(-1.1, 1.1)
ylim(-1.1, 1.1)
tick_params(labelbottom='off',
            bottom='off',
            labelleft='off',
            top='off',
            right='off',
            left='off')

print 'done with %s random broomstick corrected'%str(N)

figure(3)
suptitle(r'$\mathrm{List\/of\/chord\/length\/for\/%s \/Chords}$' %(str(N)))

subplot(1,2,1)
plot(sort(chordList1), 'k', ls = ':', label = r'$\mathrm{Wrong\/Midpoint}$')
grid(True)
ylim(0,2)
axhline(4./3, lw = 0.5, c = 'black')

plot(sort(chordList2), 'b', ls = ':', label = r'$\mathrm{Right\/Midpoint}$')
legend(loc='lower right')
axhline(4/pi, lw = 0.5, c = 'blue')

subplot(1,2,2)
r = linspace(0,1,1000)
length = 2*sqrt(r)
plot(r,length, 'black')


    
show()
