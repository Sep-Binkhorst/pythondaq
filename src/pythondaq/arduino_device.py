import pyvisa
import csv

rm = pyvisa.ResourceManager("@py")

def list_resources():
    ports = rm.list_resources()
    return ports

class ArduinoVISADevice:
    """_Samenvatting_
    """
    def __init__(self, port):
        """_

        Args:
            port (ASRL?::INSTR): Naam van de ingang van de Arduino
        """
        self.device = rm.open_resource(f"{port}", read_termination="\r\n", write_termination="\n")

    def get_identification(self):
        """_Functie voor het verkrijgen van de identificatie van je verbonden apparaat_

        Returns:
            _Ingang naam_: _Naam van de ingang van je verbonden apparaat_
        """
        identification = self.device.query("*IDN?")
        return identification
    
    def set_output_value(self, value):
        """_Functie voor het bepalen van de voltage_

        Args:
            value (_raw waarde_): _raw waarde voor de voltage dat je door je apparaat wilt laten lopen_
        """
        self.device.query(f"OUT:CH0 {value}")

    def get_output_value(self):
        """_Functie voor het meten van de voltage over kanaal 0_

        Returns:
            _raw waarde_: _raw waarde van de voltage over kanaal 0_
        """
        output = self.device.query(f"MEAS:CH0?")
        return output

    def get_input_value(self, channel):
        """_Functie voor het meten van de voltage over een gekozen kanaal_

        Args:
            channel (_integer_): _naam van de kanaal waarvan je de voltage wilt meten_

        Returns:
            _raw waarde_: _raw waarde van de voltage over de gekozen kanaal_
        """
        raw = self.device.query(f"MEAS:CH{channel}?")
        return raw

    def get_input_voltage(self, channel):
        """_Functie voor het meten van de voltage over een gekozen kanaal in Volt_

        Args:
            channel (_integer_): _naam van de kanaal waarvan je de voltage wilt meten_

        Returns:
            _voltage_: _voltage over de gekozen kanaal in Volt_
        """
        raw = self.device.query(f"MEAS:CH{channel}?")
        voltage = float(raw) * (3.3/1024)
        return voltage

help(ArduinoVISADevice)

