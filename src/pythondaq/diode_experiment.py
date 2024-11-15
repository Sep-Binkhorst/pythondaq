from pythondaq.arduino_device import ArduinoVISADevice, list_resources
import numpy as np

print(list_resources())

class DiodeExperiment:
    """_Samenvatting_
    """
    def __init__(self):
        pass

    def scan(self, start, stop, repeats):
        """_Functie dat de gemiddelde spanning, stroom en de fouten berekent voor een experiment dat een aantal keer herhaald kan worden_

        Args:
            start (_integer_): _raw waarde voor de voltage waar je wilt beginnen met meten_
            stop (_integer_): _raw waarde voor de voltage waar je wilt stoppen met meten_
            repeats (_integer_): _hoeveelheid dat je dit experiment wilt uitvoeren_

        Returns:
            _gemiddelden en fouten_: _lijsten met de gemiddelden van de spanning, stroom en van beide ook de fouten_
        """
        device = ArduinoVISADevice(port="ASRL8::INSTR")

        voltage_avrs = []
        current_avrs = []
        
        volt_devs = []
        curt_devs = []

        #Over alle voltages een aantal keer de metingen doen
        for voltage in range(start, stop):

            voltages = []
            currents = []

            #Het aantal metingen wordt bepaald door de waarde van repeats
            for repeat in range(0, repeats):

                device.set_output_value(value=voltage)

                voltage_u1 = device.get_input_voltage(channel=1)
                voltage_u2 = device.get_input_voltage(channel=2)

                voltage_led = voltage_u1 - voltage_u2
                voltages.append(voltage_led)

                current_led = voltage_u2 / 220
                currents.append(current_led)

            #Standaardafwijking berekenen van dit aantal metingen
            volt_dev = np.std(voltages)
            curt_dev = np.std(currents)

            volt_devs.append(volt_dev)
            curt_devs.append(curt_dev)

            #Gemiddelden berekenen van de voltages en currents
            voltage_avr = sum(voltages) / len(voltages)
            current_avr = sum(currents) / len(currents)

            voltage_avrs.append(voltage_avr)
            current_avrs.append(current_avr)

        volt_devs_avrs = []
        curt_devs_avrs = []

        #Wortel N wet gebruiken voor het berekenen van de fouten
        for dev in volt_devs:
            volt_dev_avr = dev/(repeats**0.5)
            volt_devs_avrs.append(volt_dev_avr)
        
        for dev in curt_devs:
            curt_dev_avr = dev/(repeats**0.5)
            curt_devs_avrs.append(curt_dev_avr)


        return voltage_avrs, current_avrs, volt_devs_avrs, curt_devs_avrs