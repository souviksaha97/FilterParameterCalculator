import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

capVal = 100e-6
resVal = 1.6
Fc = 800
#resVal = 1/(2*math.pi*Fc*capVal)
#capVal = 1/(2*math.pi*Fc*resVal)
Fc = 1/(2*math.pi*resVal*capVal)
print(resVal)
print(capVal)
print(Fc)

loadImpedance = 8

minFreq = 50
maxFreq = 8000
stepSize = 1
voltageMax = 3.3

filterType = int(input("Enter 1 for low pass, 2 for high pass : "))

impedance = []
voltage = []
phase = []

roundedFc = int(Fc/stepSize)*stepSize
fig, ax = plt.subplots(3)

for f in range(int(minFreq), int(maxFreq)+int(stepSize), int(stepSize)):
    capReactance = 1/(2*math.pi*f*capVal)
    z = math.sqrt(math.pow(resVal,2)+math.pow(capReactance,2))
    ph = -math.atan(2*math.pi*f*resVal*capVal)
    datapoint1 = (f, z)
    if filterType == 1:
        voltOut = voltageMax*(capReactance/z)
    elif filterType == 2:
        voltOut = voltageMax*(resVal/z)

    if f == roundedFc:
        ax[0].plot(f, z, 'ro')
        ax[1].plot(f, voltOut, 'ro')
        ax[2].plot(f, (ph*180)/math.pi, 'ro')
    datapoint2 = (f, voltOut)
    datapoint3 = (f, (ph*180)/math.pi)
    impedance.append(datapoint1)
    voltage.append(datapoint2)
    phase.append(datapoint3)
    
ax[0].plot(*zip(*impedance))
ax[1].plot(*zip(*voltage))
ax[2].plot(*zip(*phase))
ax[0].set_xscale('log')
ax[1].set_xscale('log')
ax[2].set_xscale('log')
ax[0].grid()
ax[1].grid()
ax[2].grid()
ax[0].set(ylabel='Impedance (ohms)')
ax[1].set(ylabel='Voltage')
ax[2].set(xlabel='Frequency (Hz)', ylabel='Phase (deg)')
ax[0].axhline(y=loadImpedance, color='green', linestyle='--')

plt.show()

 
