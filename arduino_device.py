import pyvisa
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
