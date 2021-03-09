'''
PV cell model
@author: Ferguson et al. (2013) Front. Comput. Neurosci.
'''
from brian2 import *

defaultclock.dt = 0.001*ms

# PV cell parameters
C = 90 * pF
vr = -60.6 * mV
vpeak = 2.5 * mV
c = -70 * mV
klow = 1.7 * nS/mV
khigh = 14  * nS/mV
a = 0.1 /ms
d = 0.1 * pA
vt = -43.1 *mV
b = -0.1 * nS

N = 1   # number of cells
mean_Iapp = 150  # mean Iapplied input

time = 0

# cell eqns
pv_eqs = """
Iext  : amp
k=int(v<vt)*klow+int(v>=vt)*khigh : siemens/volt
du/dt = a*(b*(v-vr)-u)            : amp
dv/dt = (k*(v-vr)*(v-vt)+Iext -u)/C : volt
"""

# define neuron group
PV = NeuronGroup(N, model=pv_eqs, reset ="v = c; u += d" , threshold="v>=vpeak")

# set excitatory drive
PV.Iext = mean_Iapp*pA

# set initial conditions for each neuron
# PV.v = rand(len(PV)) * 0.01 -0.065  # Removing random init in single cell case
PV.v = -0.065*mV

# record all spike times for the neuron group
PV_v = StateMonitor(PV, 'v', record=True)

# run for x seconds of simulated time
duration = 1 * second  # 0.01 * second

net = Network(PV,PV_v)
net.run(duration)

#### make plot of membrane potential ####
import sys
if not '-nogui' in sys.argv:
    plot(PV_v.t, PV_v[0].v/mV)
    xlabel("Time (s)")
    ylabel("Membrane Potential (mV)")
    title('PV cell model with %d pA input'%(mean_Iapp))
    show()

#### save trace to file ####
save=True
if save:
    filename = 'PV.v.dat'
    outfile = open(filename, 'w')
    t = PV_v.t/second
    v = PV_v[0].v/volt
    print("Saving results to: %s" %filename)
    for i in range(len(t)):
        line = '%s\t%s\n'%(t[i], v[i])
        outfile.write(line)
    outfile.close()






