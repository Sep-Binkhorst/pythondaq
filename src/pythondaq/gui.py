import sys
from pythondaq.diode_experiment import DiodeExperiment
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
import pyqtgraph as pg

class UserInterface(QtWidgets.QMainWindow):
    pass

    def __init__(self):

        super().__init__()

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox = QtWidgets.QVBoxLayout(central_widget)

        self.plot_widget = pg.PlotWidget()
        vbox.addWidget(self.plot_widget)

    def scan(self):
        start = 0
        stop = 1023
        repeats = 1
        port = 8

        print(f"Work in progress, scan LED")

        diodeexperiment = DiodeExperiment()
        self.voltages, self.currents, self.v_errors, self.c_errors = diodeexperiment.scan(int(start), int(stop), int(repeats), f"ASRL{port}::INSTR")

    @Slot()
    def plot(self):
        self.plot_widget(self.voltages, self.currents, pen={"color": "m", "width": 5})
        self.plot_widget.setLabel("left", "currents")
        self.plot_widget.setLabel("bottom", "voltages")

        error_bars = pg.ErrorBarItem(self.voltages, self.currents, width=2 * self.v_errors, height=2*self.c_errors)
        self.plot_widget.addItem(error_bars)

def main():
        app = QtWidgets.QApplication(sys.argv)
        ui = UserInterface()
        ui.scan()
        ui.plot()
        ui.show()
        sys.exit(app.exec())


if __name__ == "__main__":
    main()  