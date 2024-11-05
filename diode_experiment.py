from arduino_device import ArduinoVISADevice, list_resources
import math

print(list_resources())

class DiodeExperiment:

    def scan(start, stop, repeats):
        device = ArduinoVISADevice(port="ASRL8::INSTR")

        voltage_avrs = []
        current_avrs = []
        vol_dev_avrs = []
        cur_dev_avrs = []
        for repeat in range(1, repeats):

            voltages = []
            voltage_count = 0

            currents = []
            current_count = 0

        for voltage in range(start, stop):
            device.set_output_value(value=voltage)

            voltage_u1 = device.get_input_voltage(channel=1)
            voltage_u2 = device.get_input_voltage(channel=2)

            voltage_led = voltage_u1 - voltage_u2
            voltages.append(voltage_led)

            current_led = voltage_u2 / 220
            currents.append(current_led)

            voltage_count += 1
            current_count += 1

        voltage_avr = sum(voltages) / voltage_count
        current_avr = sum(currents) / current_count

        for voltage, voltage_avrs in zip(voltages, voltage_avrs):
            vol_dev = (((voltage - voltage_avrs))/len(voltages))**0.5
            vol_dev_avrs.append(vol_dev/(repeats**0.5))

        for current, current_avrs in zip(currents, current_avrs):
            cur_dev = (((current - current_avrs))/len(currents))**0.5
            cur_dev_avrs.append(cur_dev/(repeats**0.5))

            
        voltage_avrs.append(voltage_avr)
        current_avrs.append(current_avr)


        return voltage_avrs, current_avrs, vol_dev_avrs, cur_dev_avrs


        
            
            
