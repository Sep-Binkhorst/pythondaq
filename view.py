from diode_experiment import DiodeExperiment
import matplotlib.pyplot as plt

voltages, currents = DiodeExperiment.scan(start=0, stop=1023)

plt.figure()
plt.plot(voltages, currents, 'o')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.show()