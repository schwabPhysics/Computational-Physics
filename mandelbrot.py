#mandelbrot set generator. click a spot on the canvas and then click a button
'''
z = z^2 + c, where c is a complex number and z starts at zero. In order to be
a part of the set, the magnitude of Z must always be less than two.
'''
from numpy import *
import pylab as plb
import time as time

#this global variable is needed
coords = [0,0]
magnify = 0
forward = True
onePress = True


def OnPress(event):
    '''This function is connected to the button_press_event within the pylab
        module and just returns the x and y coordinates in global coords'''
    xCenter = 0
    yCenter = 0
    global onePress
    if onePress == True:
        if event.button == 1:
            xCenter= event.xdata
            yCenter= event.ydata

            global coords
            coords[0] = xCenter
            coords[1] = yCenter

            print (xCenter,yCenter)
            onePress = False

def PressZoom(event):
    '''This is a function connected to the zoom button in figure 1'''
    if event.button != 0:
        global magnify
        magnify += 4
    plb.close()
    global onePress
    onePress = True

def PressZoomOut(event):
    '''This function is connected to the zoom out button in figure 1'''
    global magnify
    if event.button != 0 and magnify !=0:
        magnify -=4
        plb.close()
        global onePress
        onePress = True

def ResetZoom(event):
    global magnify, coords, onePress
    
    if event.button != 0:
        magnify = 0
        coords = [0,0]
        plb.close()
        onePress = True

def DonePlaying(event):
    global forward
    if event.button != 0:
        forward = False
        plb.close()
        
        
    
def PlotFractal(array, xLow,xHigh,yLow,yHigh):
    '''This function takes the array calculated from the fractal function
        below and graphs the image with specified limits of x and y highs
        and lows. This is where the connection between OnPress and
        button_press_event are made'''
    figure1 = plb.figure()
    ax1 = figure1.add_axes([.1,.1,.8,.8])
    plb.imshow(array,extent = [xLow,xHigh,yLow,yHigh])
    plb.colorbar()
    plb.connect('button_press_event', OnPress)

    ax2 = figure1.add_axes([.65,0,.1,.05])
    zoomIn = plb.Button(ax2, 'Zoom In')
    zoomIn.on_clicked(PressZoom)

    ax3 = figure1.add_axes([.8,0,.1,.05])
    zoomOut = plb.Button(ax3, 'Zoom Out')
    zoomOut.on_clicked(PressZoomOut)

    ax4 = figure1.add_axes([.5,0,.1,.05])
    reset = plb.Button(ax4, 'Reset')
    reset.on_clicked(ResetZoom)

    ax5 = figure1.add_axes([.1,0,.1,.05])
    done = plb.Button(ax5, 'Done')
    done.on_clicked(DonePlaying)
    
    plb.show()


def NewHighLow(magnify, last):
    '''This function takes a magnification factor and the coordinates of
        the last click on the screen and returns the new limits for the plot
        function'''
    xCenter = last[0]
    yCenter = last[1]

    xHigh = xCenter+2*.7**magnify
    xLow = xCenter-2*.7**magnify
    yHigh = yCenter+2*.7**magnify
    yLow = yCenter-2*.7**magnify
    return xLow, xHigh, yLow, yHigh

def Fractal(last, magnify):
    '''this function generates the mandelbrot set'''
    N = 1500                                        #number of divisions for span
    iterations = 1000                                #number of iterations

    xLow, xHigh, yLow, yHigh = NewHighLow(magnify, last)
    
    a = zeros([N,N], complex)                       #this is the sample space
    x = linspace(xLow,xHigh,N)                      #making room for our points
    y = linspace(yLow,yHigh,N)

    for i in range(len(a[0])):                      #this fills the sample space with their 
        a[i] = x - 1j*(yHigh-abs(yHigh-yLow)*i/N)      #respective real and imaginary parts
        
    z = zeros([N,N],complex)
    for i in range(iterations):                     #this is the actual computation of the set
        z = z*z + a
        if mod(i,iterations/10)==0:
            print '%.2f percent done' %(float(i)/iterations*100)

    z = sqrt(z.real**2+z.imag**2)                   #find the magnitude of each value in sample space

    b = (z-z.clip(2,1E500))/(z-z.clip(2,1E500))     #creates an array of 0 and 1's where the 1 occupies 
                                                    #the space where a magnitude is less than two
    print 'Done with Calculation'
    print 'Plotting'

    PlotFractal(b*z, xLow, xHigh, yLow, yHigh)
    

    

#-------------Main Program------------------------
magnify = 0
forward = True

while forward == True:    
    Fractal(coords, magnify)

        
    
