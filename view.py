from diode_experiment import DiodeExperiment
import matplotlib.pyplot as plt

voltages, currents, v_errors, c_errors = DiodeExperiment.scan(start=0, stop=1023, repeats = 3)

plt.figure()
plt.plot(voltages, currents, 'o')
plt.errorbar(v_errors, c_errors)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.show()