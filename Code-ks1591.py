#! /bin/python
# Code --- ks1591

# Import libraries
import matplotlib.pyplot as plt
from random import randint
from math import exp
from numpy import arange
import numpy as np

# Q1

# All variables are in SI
#  time period 0--1 second
tau = 10 * 10**-3
EL = Vr = -70 * 10**-3
Vth = -40 * 10**-3
Rm = 10 * 10**6
Ie = 3.1 * 10**-9
dt = 1 * 10**-3

# Define differential equation
def integrateFire( V, t ) :
    return ( EL - V + Rm*Ie ) / tau

# Simulate neuron
time = arange( 0.0, 1.0, step=dt )
time = np.append(time, 1.0)
V = []
V.append( Vr ) # initial value of V

for i, t in enumerate( time[1:] ) :
    V.append( V[-1] + dt * integrateFire( V[-1], t - dt ) )
    if V[-1] > Vth :
        V[-1] = Vr

# Plot results
plt.figure(1)
plt.plot(time,V)
plt.xlabel("time 't' in seconds")
plt.ylabel("voltage V in Volts")
plt.title('Spiking Integrate-and-Fire Model')
plt.axis([ 0, 1, -0.075, -0.035 ])
plt.savefig("figure1.png", dpi=300, pad_inches=0.2)
plt.show()


# Q2b

# Calculate I attractor
Iattr = (Vth - EL) / Rm
IeLow = Iattr - 0.1 * 10 ** -9
Ie = IeLow

# Simulate neuron
V = []
V.append( Vr ) # initial value of V
for i, t in enumerate( time[1:] ) :
    V.append( V[-1] + dt * integrateFire( V[-1], t - dt ) )
    if V[-1] > Vth :
        V[-1] = Vr

# Print results
plt.figure(2)
plt.plot(time,V)
plt.xlabel("time 't' in seconds")
plt.ylabel("voltage V in Volts")
plt.title('Spiking Integrate-and-Fire Model')
plt.axis([ 0, 1, -0.075, -0.035 ])
plt.savefig("figure2b.png", dpi=300, pad_inches=0.2)
plt.show()


# Q3

# Calculate currents
currents = arange( 2, 5, step=0.1 )
currents = np.append(currents, 5)
currents[:] = [ x* 10**-9 for x in currents ]

# Simulate spiking
cSpike = []
for c in currents :
    spikes = 0
    Ie = c
    V = []
    V.append( Vr ) # initial value of V
    for i, t in enumerate( time[1:] ) :
        V.append( V[-1] + dt * integrateFire( V[-1], t - dt ) )
        if V[-1] > Vth :
            V[-1] = Vr
            spikes += 1
    cSpike.append( spikes )


# Print results
plt.figure(3)
plt.plot(currents,cSpike)
plt.xlabel("current 'Ie' in Ampers")
plt.ylabel("number of spikes")
plt.title('Dependance between Input Current and Spiking Rate')
plt.axis([ 1.5*10**-9, 5.5*10**-9, -10, 120 ])
plt.savefig("figure3.png", dpi=300, pad_inches=0.2)
plt.show()


# Q4

# Define parameters
tauM =   20 * 10 ** -3 #
EL   =  -70 * 10 ** -3 #
Vr   =  -80 * 10 ** -3 #
Vth  =  -54 * 10 ** -3 #
RmIe =   18 * 10 ** -3 #
# --
RmGs = 0.15            #
Pmax =  0.5            #
tauS =   10 * 10 ** -3 #
# --
dt   =    1 * 10 ** -3 #

# Define model --- equation
def integrateFire2( V, t, tf ) :
    return ( EL - V - RmGs*( Pmax*exp(-(t-tf)/tauS) )*(V-Es) + RmIe ) / tauM

# Q4a
Es = 0
VaStart = randint(Vr * 10 **3, Vth * 10 **3) * 10 ** -3 # inclusive
VbStart = randint(Vr * 10 **3, Vth * 10 **3) * 10 ** -3 # inclusive
time = arange( 0.0, 1.0, step=dt )
time = np.append(time, 1.0)

# Simulate
Va = []
Va.append( VaStart )
tfa = 0
Vb = []
Vb.append( VbStart )
tfb = 0

for t in time[1:] :
    Va.append( Va[-1] + dt * integrateFire2( Va[-1], t - dt, tfb ) )
    Vb.append( Vb[-1] + dt * integrateFire2( Vb[-1], t - dt, tfa ) )
    if Va[-1] > Vth :
        Va[-1] = Vr
        tfa = t
    if Vb[-1] > Vth :
        Vb[-1] = Vr
        tfb = t

# Print results
plt.figure(4)
p1, = plt.plot(time,Va,'g')
p2, = plt.plot(time,Vb,'r')
plt.xlabel("time 't' in seconds")
plt.ylabel("voltage 'V' in Volts")
plt.title("Spiking Integrate-and-Fire Model \n of two neurons synapticly connected \n with excitatory synapses")
plt.legend([p2, p1], ["Neuron B", "Neuron A"])
plt.axis([ 0, 1, -0.085, -0.050 ])
plt.subplots_adjust(top=0.8)
plt.savefig("figure4a.png", dpi=300, pad_inches=0.2)
plt.show()

# Q4b

# Simulate neurons
Es = -80 * 10 ** -3
VaStart = randint(Vr * 10 **3, Vth * 10 **3) * 10 ** -3 # inclusive
VbStart = randint(Vr * 10 **3, Vth * 10 **3) * 10 ** -3 # inclusive
time = arange( 0.0, 1.0, step=dt )
time = np.append(time, 1.0)

Va = []
Va.append( VaStart )
tfa = 0  # ???????????????????
Vb = []
Vb.append( VbStart )
tfb = 0 # ???????????????????

for t in time[1:] :
    Va.append( Va[-1] + dt * integrateFire2( Va[-1], t - dt, tfb ) )
    Vb.append( Vb[-1] + dt * integrateFire2( Vb[-1], t - dt, tfa ) )
    if Va[-1] > Vth :
        Va[-1] = Vr
        tfa = t
    if Vb[-1] > Vth :
        Vb[-1] = Vr
        tfb = t

# Print results
plt.figure(5)
p1, = plt.plot(time,Va,'g')
p2, = plt.plot(time,Vb,'r')
plt.xlabel("time 't' in seconds")
plt.ylabel("voltage 'V' in Volts")
plt.title("Spiking Integrate-and-Fire Model \n of two neurons synapticly connected \n with inhibitory synapses")
plt.legend([p2, p1], ["Neuron B", "Neuron A"])
plt.axis([ 0, 1, -0.085, -0.050 ])
plt.subplots_adjust(top=0.8)
plt.savefig("figure4b.png", dpi=300, pad_inches=1)
plt.show()

# EOF #
