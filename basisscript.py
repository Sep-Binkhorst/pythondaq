import pyvisa
import matplotlib.pyplot as plt
import time
import csv

rm = pyvisa.ResourceManager("@py")

def list_resources():
    ports = rm.list_resources()
    return ports

class ArduinoVISADevice:
    def __init__(self, port):
        self.device = rm.open_resource(f"{port}", read_termination="\r\n", write_termination="\n")

    def get_identification(self):
        identification = self.device.query("*IDN?")
        return identification
    
    def set_output_value(self, value):
        self.device.query(f"OUT:CH0 {value}")

    def get_output_value(self):
        output = self.device.query(f"MEAS:CH0?")
        return output

    def get_input_value(self, channel):
        raw = self.device.query(f"MEAS:CH{channel}?")
        return raw

    def get_input_voltage(self, channel):
        raw = self.device.query(f"MEAS:CH{channel}?")
        voltage = float(raw) * (3.3/1024)
        return voltage


# #Controller bouwen opdrachten
# print(list_resources())

# Create an instance for the Arduino on port "ASRL28::INSTR"
device = ArduinoVISADevice(port="ASRL8::INSTR")

# # print identification string
# identification = device.get_identification()
# print(identification)

# # set OUTPUT voltage on channel 0, using ADC values (0 - 1023)
# device.set_output_value(value=828)

# # measure the voltage on INPUT channel 2 in ADC values (0 - 1023)
# ch2_value = device.get_input_value(channel=2)
# print(f"{ch2_value=}")

# # measure the voltage on INPUT channel 2 in volts (0 - 3.3 V)
# ch2_voltage = device.get_input_voltage(channel=2)
# print(f"{ch2_voltage=}")

# # get the previously set OUTPUT voltage in ADC values (0 - 1023)
# ch0_value = device.get_output_value()
# print(f"{ch0_value=}")


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

#Controller Afsplitsen Opdracht

