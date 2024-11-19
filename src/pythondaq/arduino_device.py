import pyvisa

rm = pyvisa.ResourceManager("@py")

def list_resources():
    ports = rm.list_resources()
    return ports

class ArduinoVISADevice:
    """Class that has functions that can communicate with the Arduino.
    """
    def __init__(self, port):
        """_

        Args:
            port (ASRL?::INSTR): Name of the port of the Arduino_
        """
        self.device = rm.open_resource(f"{port}", read_termination="\r\n", write_termination="\n")

    def get_identification(self):
        """_Function that provied the identification of your connected device_

        Returns:
            _Identification_: _Information of your connected device_
        """
        identification = self.device.query("*IDN?")
        return identification
    
    def set_output_value(self, value):
        """_Function for measuring the voltage_

        Args:
            value (_raw value_): _raw value of the voltage you want to apply to your connected device_
        """
        self.device.query(f"OUT:CH0 {value}")

    def get_output_value(self):
        """_Function for measuring the voltage of channel 0_

        Returns:
            _raw value_: _raw value of the voltage of channel 0_
        """
        output = self.device.query(f"MEAS:CH0?")
        return output

    def get_input_value(self, channel):
        """_Function that measures the voltage of a chosen channel_

        Args:
            channel (_integer_): _name of the channel you wish to measure the voltage of_

        Returns:
            _raw value_: _raw value of the voltage of your chosen channel_
        """
        raw = self.device.query(f"MEAS:CH{channel}?")
        return raw

    def get_input_voltage(self, channel):
        """_Function for measuring the voltage of a chosen channel in Volts_

        Args:
            channel (_integer_): _name of the channel you wish to know the voltage of_

        Returns:
            _voltage_: _voltage of the chosen channel in Volts_
        """
        raw = self.device.query(f"MEAS:CH{channel}?")
        voltage = float(raw) * (3.3/1024)
        return voltage

