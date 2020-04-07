import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math


unknownVar = input("R for Resistance, C for Capacitance, F for Frequency : ")

if unknownVar == 'R':
    capVal = float(input("Enter Capacitance : "))
    Fc = float(input("Enter cutoff frequency : "))
    resVal = 1/(2*math.pi*Fc*capVal)
    print("Resistance = ", resVal)

elif unknownVar == 'C':
    resVal = float(input("Enter Resistance : "))
    Fc = float(input("Enter cutoff frequency : "))
    capVal = 1/(2*math.pi*Fc*resVal)
    print("Capacitance = ", capVal)

elif unknownVar == 'F':
    resVal = float(input("Enter Resistance : "))
    capVal = float(input("Enter Capacitance : "))
    Fc = 1/(2*math.pi*resVal*capVal)
    print("Cutoff Frequency = ", Fc)
# capVal = 100e-6
# resVal = 10
#resVal = 1/(2*math.pi*Fc*capVal)
#capVal = 1/(2*math.pi*Fc*resVal)
# Fc = 1/(2*math.pi*resVal*capVal)
print(resVal)
print(capVal)
print(Fc)
# print("Resistance = ", resVal)
# print(capVal)
# print(Fc)

loadImpedance = float(input("Enter required load impedance. Enter 0 if not required : "))

minFreq = float(input("Enter minimum frequency : "))
if minFreq == 0:
    minFreq = 1
maxFreq = float(input("Enter maximum frequency : "))
stepSize = int(input("Enter step size : "))
voltageMax = float(input("Enter voltage range : "))

filterType = int(input("Enter 1 for low pass, 2 for high pass : "))
filterOrder = int(input("Enter order of filter : "))

print("Please wait..")

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
        ax[0].plot(f, z, 'ro', label='$f = Cutoff Frequency')
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

if loadImpedance != 0:
    ax[0].axhline(y=loadImpedance, color='green', linestyle='--', label='Load Impedance')

plt.show()

 
