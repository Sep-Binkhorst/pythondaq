import pyvisa
import matplotlib.pyplot as plt
import time
import csv

rm = pyvisa.ResourceManager("@py")

def list_resources():
    ports = rm.list_resources
    return ports

class ArduinoVISADevice:
    def __init__(self, port):
        self.device = rm.open_resource(f"{port}", read_termination="\r\n", write_termination="\n")

    def get_identification(self):
        identification = self.device.query("*IDN?")
        return identification
    
    def set_output_value(self, value):
        self.device.query(f"OUT:CH0 {value}")

    def get_input_value(self, channel):
        raw = self.device.query(f"MEAS:CH{channel}")
        return raw

    def get_input_voltage(self, channel):
        raw = self.device.query(f"MEAS:CH{channel}")
        voltage = float(raw) * (3.3/1024)
        return voltage

print(list_resources())

# Create an instance for the Arduino on port "ASRL28::INSTR"
device = ArduinoVISADevice(port="ASRL8::INSTR")

# print identification string
identification = device.get_identification()
print(identification)

# set OUTPUT voltage on channel 0, using ADC values (0 - 1023)
device.set_output_value(value=828)

# measure the voltage on INPUT channel 2 in ADC values (0 - 1023)
ch2_value = device.get_input_value(channel=2)
print(f"{ch2_value=}")

# measure the voltage on INPUT channel 2 in volts (0 - 3.3 V)
ch2_voltage = device.get_input_voltage(channel=2)
print(f"{ch2_voltage=}")

# get the previously set OUTPUT voltage in ADC values (0 - 1023)
ch0_value = device.get_output_value()
print(f"{ch0_value=}")

# voltages = []
# currents = []
# for voltage in range(0, 1023):
#     device.query(f"OUT:CH0 {voltage}")

#     raw_u2 = device.query(f"MEAS:CH2?")
#     # print(f"De raw voltage op de weerstand is {raw_u2}")

#     voltage_u2 = float(raw_u2) * (3.3/1024)
#     # print(f"De voltage op de weerstand is {voltage_u2}")

#     raw_u1 = device.query(f"MEAS:CH1?")
#     voltage_u1 = float(raw_u1) * (3.3/1024)

#     raw_led = float(raw_u1) - float(raw_u2)

#     voltage_led = voltage_u1 - voltage_u2
#     voltages.append(voltage_led)

#     current_led = voltage_u2 / 220
#     currents.append(current_led)

#     # print(f"De raw voltage op de led is {raw_led}")
#     # print(f"De voltage op de led is {voltage_led}")

# # plt.figure()
# # plt.plot(voltages, currents, 'o')
# # plt.xlabel('Voltage (V)')
# # plt.ylabel('Current (A)')
# # plt.show()

# for voltage, current in zip(voltages, currents):
#     print(f"Voltage is {voltage} en current is {current} en de weerstand is 220")

# with open('metingen.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['voltage', 'current'])
#     for voltage, current in zip(voltages, currents):
#         writer.writerow([voltage, current])