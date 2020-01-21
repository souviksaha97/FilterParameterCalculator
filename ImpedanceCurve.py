import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

capVal = 100e-6
resVal = 1.6
Fc = 1000
#resVal = 1/(2*math.pi*Fc*capVal)
print(resVal)
print(capVal)
loadImpedance = 8

minFreq = 100
maxFreq = 20000
stepSize = 5
voltageMax = 3.3
#iteration = (maxFreq-minFreq)/stepSize
impedance = []
voltage = []

fig, ax = plt.subplots(2)
#plt.xlim(left=maxFreq+stepSize, x=minFreq)


for f in range(int(minFreq), int(maxFreq)+int(stepSize), int(stepSize)):
    capReactance = 1/(2*math.pi*f*capVal)
    z = math.sqrt(math.pow(resVal,2)+math.pow(capReactance,2))
    datapoint1 = (f, z)
    voltOut = voltageMax*(capReactance/z)
    datapoint2 = (f, voltOut)
    impedance.append(datapoint1)
    voltage.append(datapoint2)
    
    #freq.append(f)
    #print(z)
    #print(f)
    
#plt.line(f, z)
ax[0].plot(*zip(*impedance))
ax[1].plot(*zip(*voltage))
ax[0].set_xscale('log')
ax[1].set_xscale('log')
ax[0].grid()
ax[1].grid()
ax[0].set(ylabel='Impedance (ohms)')
ax[1].set(xlabel='Frequency (Hz)', ylabel='Voltage')
#plt.xlim(minFreq, maxFreq+stepSize)
fig.savefig("r1.6c100e-6.png")
plt.show()

 
