# main.py: The falling cat in interactive 3D.
#            Note the use of the Euler integration method.

# import packages
from enthought.mayavi.mlab import axes,plot3d
from numpy import arange, array
import pylab as py
from scipy import *
from scipy.integrate import odeint

# import my functions
from RK3D import RK3D, RK3DList
from EOM import EOM

# print manual for maya
print """
	Rotate: Left-click & drag
	Zoom:   Right-Click & slide up/down
	Slide:  Middle-Click & drag
"""


###
### define original functions
###

# define the function modular
# this change range of angle to [-pi, pi]
def mod(data):
    len = size(data)
    for i in xrange(len):
        angle = data[i]
        if angle == 0:
            result = angle
            #return result
        elif angle > 0:
            temp = angle + pi
            temp2 = (temp - temp%(2*pi)) / (2*pi)
            result = angle - (2*pi)*temp2
            #return result
        else:
            temp = angle - pi
            temp2 = (temp - temp%(-2*pi)) / (2*pi)
            result = angle - (2*pi)*temp2
            #return result
        
        data[i] = result
    
    return data

# define function jump which find jump point
# find uncontinuous points from data
def jump(data):
    len = size(data)-1
    result=[]
    for i in xrange(len):
        if (data[i]*data[i+1]<0 and abs(data[i])>1.0):
           result.append(i)

    return result

# define function flatten
# make one list from several list
def flatten(L):
    if type(L) != type([]): 
        return [L]
    if L == []: 
        return L
    return flatten(L[0]) + flatten(L[1:])

# define function which delete same number
def delsame(L):
    len = size(L)-1
    result = []
    for i in xrange(len):
        if L[i] != L[i+1]:
            result.append(L[i])
    if L[len-2] != L[len-1]:
        result.append(L[len])
    return result
    

# Integration time step
dt = 0.001

# Torque parameters
# change these variables
T1 = 1.0
T2 = 0.0
T3 = 0.0
para = array([T1, T2, T3])

# Initial conditions
q1 = 0.0
q2 = 1.0
q3 = 0.0
q4 = 0.0
q5 = 0.0
q6 = pi / 12.0
q7 = 0.0
q8 = 0.0
q9 = - pi / 6.0
u1 = 0.0
u2 = 0.0
u3 = 0.0
u4 = 0.0
u5 = 0.0
u6 = 0.0
u7 = 0.0
u8 = 0.0
u9 = 0.0
IC = array([q1, q2, q3, q4, q5, q6, q7, q8, q9, u1, u2, u3 ,u4, u5, u6, u7, u8, u9])

# the number of iteration
N = 1000

# Store the trajectory using runge-kutta method
# Time, variables = RK3DList(EOM, para, state, dt, N)

Time  = arange(0,(N*dt),dt)
# calculate the trajectory using scipy function
variables = odeint(EOM, IC, Time, (para,))

# save the data
Trajq1, Trajq2, Trajq3, Trajq4, Trajq5, Trajq6,Trajq7, Trajq8, Trajq9,\
Traju1, Traju2, Traju3, Traju4, Traju5, Traju6,Traju7, Traju8, Traju9 = transpose(variables)


'''
# calculate the data mod[-pi,pi]
Trajq4m = mod(Trajq4)
Trajq5m = mod(Trajq5)
Trajq6m = mod(Trajq6)
Trajq7m = mod(Trajq7)
Trajq8m = mod(Trajq8)
Trajq9m = mod(Trajq9)
'''

# plot each plot using plot3d
plot3d(Trajq4, Trajq5, Trajq6, Time, color = (0.0, 0.0, 1.0), tube_radius = 0.1)
#plot3d(mod(Trajq4), mod(Trajq5), mod(Trajq6), Time, color = (1.0, 0.0, 0.0), tube_radius = 0.01)
axes(color=(0.,0.,0.),extent=[-pi,pi,-pi,pi,-pi,pi],ranges=[-pi,pi,-pi,pi,-pi,pi])



'''
# calculate the jonping point
point1 = jump(Trajq4m)
point2 = jump(Trajq5m)
point3 = jump(Trajq6m)
point = [point1, point2, point3]
point = flatten(point)
point = sorted(point)
point = delsame(point)

# plot 3D using the data of range [-pi, pi] 
for j in xrange(size(point)):
    stop = point[j]
    if size(point)==1:
        plot3d(Trajq4m[0:point[j]], Trajq5m[0:point[j]], Trajq6m[0:point[j]], color = (1.0, 0.0, 0.0), tube_radius = 0.01)
        plot3d(Trajq4m[point[j]+1:N+1], Trajq5m[point[j]+1:N+1], Trajq6m[point[j]+1:N+1], color = (0.0, 0.0, 1.0), tube_radius = 0.01)

    else:
        if j == 1:
            plot3d(Trajq4m[0:point[j]], Trajq5m[0:point[j]], Trajq6m[0:point[j]], color = (1.0, 0.0, 0.0), tube_radius = 0.01)
        elif j == size(point)-1:
            plot3d(Trajq4m[point[j]+1:N+1], Trajq5m[point[j]+1:N+1], Trajq6m[point[j]+1:N+1], color = (0.0, 0.0, 1.0), tube_radius = 0.01)
        else:
            if (point[j]+1) == point[j+1]:
                plot3d(float(Trajq4m[point[j]+1]), float(Trajq5m[point[j]+1]), float(Trajq6m[point[j]+1]), color = (0.0, 1.0, 0.0), tube_radius = 0.01) 
            else:
                plot3d(Trajq4m[point[j]+1:point[j+1]], Trajq5m[point[j]+1:point[j+1]], Trajq6m[point[j]+1:point[j+1]], color = (0.0, 1.0, 0.0), tube_radius = 0.01)   

#axes(color=(0.,0.,0.),extent=[-pi,pi,-0.5,0.5,-0.5,0.5],ranges=[-pi,pi,-0.5,0.5,-0.5,0.5])
axes(color=(0.,0.,0.),extent=[-pi,pi,-pi,pi,-pi,pi],ranges=[-pi,pi,-pi,pi,-pi,pi])

#plot the result
#py.plot(Time, Trajq2)
#py.plot(Time, Trajq5)
#py.plot(Time, Trajq4)
py.figure(1)
for i in xrange(N):
    py.plot([Time[i]], [Trajq4m[i]], 'b,')
    py.plot([Time[i]], [Trajq5m[i]], 'g,')
    py.plot([Time[i]], [Trajq6m[i]], 'r,')

'''
###
### plot the results
###
# plot q5 vs. q6 graph
py.figure(1)
TitleString = '(T1, T2, T3) = (%g, %g, %g)' % (T1, T2, T3)
TitleString += ', dt = %g' % (dt)
py.title(TitleString)
py.xlabel('q5 [rad]')
py.ylabel('q6 [rad]')
py.plot(Trajq5, Trajq6,'b-')

# plot q8 vs. q9 graph
py.figure(2)
TitleString = '(T1, T2, T3) = (%g, %g, %g)' % (T1, T2, T3)
TitleString += ', dt = %g' % (dt)
py.title(TitleString)
py.xlabel('q8 [rad]')
py.ylabel('q9 [rad]')
py.plot(Trajq8, Trajq9,'b-')

# plot q4, q5, q6
py.figure(3)
for i in xrange(N):
    py.plot([Time[i]], [Trajq4[i]], 'b,')
    py.plot([Time[i]], [Trajq5[i]], 'g,')
    py.plot([Time[i]], [Trajq6[i]], 'r,')

# plot q4, q5, q6
py.figure(4)
py.subplot(3, 1, 1)
TitleString = '(T1, T2, T3) = (%g, %g, %g)' % (T1, T2, T3)
TitleString += ', dt = %g' % (dt)
py.title(TitleString)
py.ylabel('q4 [rad]')
py.plot(Time, Trajq4)
py.subplot(3, 1, 2)
py.ylabel('q5 [rad]')
py.plot(Time, Trajq5)
py.subplot(3, 1, 3)
py.xlabel('Time [s]')
py.ylabel('q6 [rad]')
py.plot(Time, Trajq6)

# plot q7, q8, q9
py.figure(5)
py.subplot(3, 1, 1)
TitleString = '(T1, T2, T3) = (%g, %g, %g)' % (T1, T2, T3)
TitleString += ', dt = %g' % (dt)
py.title(TitleString)
py.ylabel('q7 [rad]')
py.plot(Time, Trajq7)
py.subplot(3, 1, 2)
py.ylabel('q8 [rad]')
py.plot(Time, Trajq8)
py.subplot(3, 1, 3)
py.xlabel('Time [s]')
py.ylabel('q9 [rad]')
py.plot(Time, Trajq9)

# show the graph
py.show()
