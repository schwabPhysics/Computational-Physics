#Lorenz Equations. This is an example from Mark Newman's book - Computational Physics.
#it is just a quick visualization of the "determined randomness"

import pylab as plb


sigma = 10; r = 28; b = 8./3

x = [0]; y = [1]; z = [0]

dt = 0.01
time = [t/100. for t in range(10001)]
for t in range(len(time)-1):
    dx = sigma*(y[t]-x[t])*dt
    dy = (r*x[t]-y[t]-x[t]*z[t])*dt
    dz = (x[t]*y[t]-b*z[t])*dt

    x.append(x[t] + dx)
    y.append(y[t] + dy)
    z.append(z[t] + dz)

plb.subplot(1,2,1)
plb.title('the x-z plane')
plb.plot(x,z, color = 'green')

plb.subplot(1,2,2)
plb.title('y-position over time')
plb.plot(y,time, color = 'red')


plb.show()
