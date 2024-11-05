from arduino_device import ArduinoVISADevice, list_resources
import matplotlib.pyplot as plt

# Create an instance for the Arduino on port "ASRL28::INSTR"
device = ArduinoVISADevice(port="ASRL8::INSTR")

#Controller Implementeren Opdracht
voltages = []
currents = []
for voltage in range(0, 1023):
    device.set_output_value(value=voltage)

    voltage_u1 = device.get_input_voltage(channel=1)
    voltage_u2 = device.get_input_voltage(channel=2)

    voltage_led = voltage_u1 - voltage_u2
    voltages.append(voltage_led)

    current_led = voltage_u2 / 220
    currents.append(current_led)

plt.figure()
plt.plot(voltages, currents, 'o')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.show()
