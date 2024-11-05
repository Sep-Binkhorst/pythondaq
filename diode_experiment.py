from arduino_device import ArduinoVISADevice, list_resources

print(list_resources())

class DiodeExperiment:

    def scan(start, stop):
        device = ArduinoVISADevice(port="ASRL8::INSTR")

        voltages = []
        currents = []

        for voltage in range(start, stop):
            device.set_output_value(value=voltage)

            voltage_u1 = device.get_input_voltage(channel=1)
            voltage_u2 = device.get_input_voltage(channel=2)

            voltage_led = voltage_u1 - voltage_u2
            voltages.append(voltage_led)

            current_led = voltage_u2 / 220
            currents.append(current_led)
        
        return voltages, currents
