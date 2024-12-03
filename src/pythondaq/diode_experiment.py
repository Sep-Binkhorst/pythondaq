from pythondaq.arduino_device import ArduinoVISADevice, list_resources
import numpy as np


class DiodeExperiment:
    """Class that can perform an experiment with the function scan() using the Arduino.
    """
    def __init__(self):
        pass

    def scan(self, start, stop, repeats, port):
        """_Function that calculates the average voltages, currents and errors for a predetermined experiment._

        Args:
            start (_integer_): _raw value for the voltage where you want to start measuring
            stop (_integer_): _raw value for the voltage where you want to stop measuring
            repeats (_integer_): _amount of times you want this experiment to be repeated_

        Returns:
            _Averages and errors_: _lists with the averages of the voltages, currents and the errors on both these lists_
        """
        self.device = ArduinoVISADevice(port)

        voltage_avrs = []
        current_avrs = []
        
        volt_devs = []
        curt_devs = []

        #Change the unit of your voltage from Volts to raw-value
        start = start * (1023/3.3)
        stop = stop * (1023/3.3)

        #Perform measurements within a predetermined range
        for voltage in range(int(start), int(stop)):

            voltages = []
            currents = []

            #Perform all these measurements a certain amount of times.
            for repeat in range(0, repeats):

                self.device.set_output_value(value=voltage)

                voltage_u1 = self.device.get_input_voltage(channel=1)
                voltage_u2 = self.device.get_input_voltage(channel=2)

                voltage_led = voltage_u1 - voltage_u2
                voltages.append(voltage_led)

                current_led = voltage_u2 / 220
                currents.append(current_led)
            

            #Calcute the standard deviation over these measurements
            volt_dev = np.std(voltages)
            curt_dev = np.std(currents)

            volt_devs.append(volt_dev)
            curt_devs.append(curt_dev)

            #Calculate the average errors of your voltages and currents
            voltage_avr = sum(voltages) / len(voltages)
            current_avr = sum(currents) / len(currents)

            voltage_avrs.append(voltage_avr)
            current_avrs.append(current_avr)

        volt_devs_avrs = []
        curt_devs_avrs = []

        self.device.set_output_value(0)

        #Use the square root of N rule to calculate the final errors and put them in lists
        for dev in volt_devs:
            volt_dev_avr = dev/(repeats**0.5)
            volt_devs_avrs.append(volt_dev_avr)
        
        for dev in curt_devs:
            curt_dev_avr = dev/(repeats**0.5)
            curt_devs_avrs.append(curt_dev_avr)


        return voltage_avrs, current_avrs, volt_devs_avrs, curt_devs_avrs
    
    def close(self):
        self.device.close_arduino()