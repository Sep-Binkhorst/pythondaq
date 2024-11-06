from diode_experiment import DiodeExperiment
import matplotlib.pyplot as plt

diodeexperiment = DiodeExperiment()
voltages, currents, v_errors, c_errors = diodeexperiment.scan(start=0, stop=1023, repeats = 3)

plt.figure()
plt.plot(voltages, currents, 'o')
plt.errorbar(v_errors, c_errors)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.show()