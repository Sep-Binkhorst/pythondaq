from pythondaq.arduino_device import list_resources, ArduinoVISADevice
from pythondaq.diode_experiment import DiodeExperiment
import click
import csv


@click.group()
def cmd_group():
    pass


@cmd_group.command("")

def list():
    print(f"Work in progress, list devices")
    print(list_resources())

@cmd_group.command("info")

@click.argument("name")

def info(name):
    device = ArduinoVISADevice(name)
    print(device.get_identification())
    
@cmd_group.command("")
@click.option(
    "--start",
    default=0,
    show_default=True
)

@click.argument("stop")

@click.option(
    "--repeats",
    default=1,
    show_default=True
)

@click.option(
    "--output",
    default=None
)

@click.argument("port")

def scan(start, stop, repeats, output, port):
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