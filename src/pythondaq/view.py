from pythondaq.diode_experiment import DiodeExperiment
import matplotlib.pyplot as plt
import csv

def main():
    """Main function in this script that runs the experiment. It plots the experiment with the errors and creates a csv file.

    Returns:
        Lists: Returns the lists with the voltages, currents and the errors for both lists.
    """
    diodeexperiment = DiodeExperiment()
    voltages, currents, v_errors, c_errors = diodeexperiment.scan(start=0, stop=1023, repeats = 3, port="ASRL8::INSTR")

    plt.figure()
    plt.errorbar(voltages, currents, xerr=v_errors, yerr=c_errors, fmt='o', ecolor='r')
    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (A)')
    plt.show()

    with open('metingen.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Voltages', 'Currents', 'V_errors', 'C_errors'])
        for voltage, current, v_error, c_error in zip(voltages, currents, v_errors, c_errors):
            writer.writerow([voltage, current, v_error, c_error])

    return voltages, currents, v_errors, c_errors

if __name__=="__main__":
    main()