# RK3D.py: Define functions 4th Runge-kutta metthod
#
# RK3D: 3D fourth-order runge-kutta
# 
# input
#  function: function name
#  parameters: list of parameters
#  state: list of initial condition
#  dt: time step
#
# output
#  newstate: calculated new state
#
# RK3DList: calculate list of state using 3D fourth-order runge-kutta method
# 
# input
#  function: function name
#  parameters: list of parameters
#  state: list of initial condition
#  dt: time step
#  N: the number of iteration
#
# output
#  transpose(state): list of state


from numpy import *

# define function RK3D
# calculate next values
def RK3D(function, parameters, state, dt):
   k1 = dt * function(parameters, state)
   k2 = dt * function(parameters, (state + k1 / 2.0))
   k3 = dt * function(parameters, (state + k2 / 2.0))
   k4 = dt * function(parameters, (state + k3))
   newstate = state + (k1 + 2. * k2 + 2. * k3 + k4) / 6.0

   return newstate

# define function RK3DList
# calculate lists of variables
def RK3DList(function, parameters, state, dt, N):
   newstate = state
   time = array([0])
   #time = [0]
   for i in xrange(N):
      newstate = RK3D(function, parameters, newstate, dt)
      state = append(state, newstate, axis = 0)
      #time.append((i+1)*dt)
      time = append(time, (i+1)*dt)

   #result = append(time, transpose(state)[0], axis = 0)

   return time, transpose(state)
   #return result
   

   
