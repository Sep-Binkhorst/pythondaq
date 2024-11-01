import pyvisa
import matplotlib.pyplot as plt
import time
import csv

rm = pyvisa.ResourceManager("@py")

device = rm.open_resource(
    "ASRL8::INSTR", read_termination="\r\n", write_termination="\n")

voltages = []
currents = []
for voltage in range(0, 1023):
    device.query(f"OUT:CH0 {voltage}")

    raw_u2 = device.query(f"MEAS:CH2?")
    # print(f"De raw voltage op de weerstand is {raw_u2}")

    voltage_u2 = float(raw_u2) * (3.3/1024)
    # print(f"De voltage op de weerstand is {voltage_u2}")

    raw_u1 = device.query(f"MEAS:CH1?")
    voltage_u1 = float(raw_u1) * (3.3/1024)

    raw_led = float(raw_u1) - float(raw_u2)

    voltage_led = voltage_u1 - voltage_u2
    voltages.append(voltage_led)

    current_led = voltage_u2 / 220
    currents.append(current_led)

    # print(f"De raw voltage op de led is {raw_led}")
    # print(f"De voltage op de led is {voltage_led}")

# plt.figure()
# plt.plot(voltages, currents, 'o')
# plt.xlabel('Voltage (V)')
# plt.ylabel('Current (A)')
# plt.show()

for voltage, current in zip(voltages, currents):
    print(f"Voltage is {voltage} en current is {current} en de weerstand is 220")

with open('metingen.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['voltage', 'current'])
    for voltage, current in zip(voltages, currents):
        writer.writerow([voltage, current])