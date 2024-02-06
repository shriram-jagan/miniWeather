import numpy as np

# these values should be same as that in the makefile
nx = 200
nz = 100
hs = 2 
nvariables = 4
ntimesteps = 11
filename = "state.txt"

# shape of the array will be (ntimesteps, nvariables, nz+2*hs, nx+2*hs)
array_shape = (ntimesteps, nvariables, nz + 2*hs, nx + 2*hs)

x = np.loadtxt(filename, delimiter=",").reshape(array_shape)

for timestep in range(ntimesteps):
    for variable in range(nvariables):
        state = x[timestep][variable]

        #process state
