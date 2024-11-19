from pythondaq.arduino_device import list_resources, ArduinoVISADevice
from pythondaq.diode_experiment import DiodeExperiment
import click
import csv


@click.group()
def cmd_group():
    pass


@cmd_group.command("")

def list():
    """This function creates a list of all connected devices.
    """
    print(f"Work in progress, list devices")
    print(list_resources())

@cmd_group.command("info")

@click.argument("name")

def info(name):
    """This function shows information about your chosen device with name NAME.

    Args:
        name (string): NAME of the device you wish to have information of.
    """
    device = ArduinoVISADevice(name)
    print(device.get_identification())
    
@cmd_group.command("")
@click.option(
    "--start",
    default=0,
    help='Starting value for the range you want to measure.',
    show_default=True
)

@click.argument("stop")

@click.option(
    "--repeats",
    default=1,
    help='Amount of times you wish to repeat your measurements.',
    show_default=True
)

@click.option(
    "--output",
    default=None,
    help='Name for the csv file you wish to create.',
    show_default=True
)

@click.argument("port")


def scan(start, stop, repeats, output, port):
    """Scan function for the voltages and currents of your connected device. 

    Args:
        start (integer): Starting value for where you want to start measuring.
        stop (integer): Ending value for the range you want to measure.
        repeats (integer): Amount of times you want to repeat your measurements.
        output (string): Name of the csv file of your measurements.
        port (string): Name of the port of your device.
    """
    print(f"Work in progress, scan LED")

    diodeexperiment = DiodeExperiment()
    voltages, currents, v_errors, c_errors = diodeexperiment.scan(int(start), int(stop), int(repeats), port)

    print(voltages)
    print(currents)

    if output != None:
        with open(f'{output}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Voltages', 'Currents'])
            for voltage, current in zip(voltages, currents):
                writer.writerow([voltage, current])