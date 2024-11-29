import sys
from pythondaq.diode_experiment import DiodeExperiment, list_resources
from pythondaq.arduino_device import ArduinoVISADevice
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
import pyqtgraph as pg
import numpy as np
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

class UserInterface(QtWidgets.QMainWindow):
    pass

    def __init__(self):

        super().__init__()

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vbox = QtWidgets.QVBoxLayout(central_widget)

        lhbox = QtWidgets.QHBoxLayout()
        shbox = QtWidgets.QHBoxLayout()
        vbox.addLayout(lhbox)
        vbox.addLayout(shbox)

        strlabel = QtWidgets.QLabel("Start (V)")
        stplabel = QtWidgets.QLabel("Stop (V)")
        numlabel = QtWidgets.QLabel("Repeats")

        lhbox.addWidget(strlabel)
        lhbox.addWidget(stplabel)
        lhbox.addWidget(numlabel)

        self.start = QtWidgets.QDoubleSpinBox()
        self.start.setMinimum(0)
        self.start.setValue(0)

        self.stop = QtWidgets.QDoubleSpinBox()
        self.stop.setMaximum(3.3)
        self.stop.setValue(0)

        self.num = QtWidgets.QDoubleSpinBox()
        self.num.setMinimum(0)
        self.num.setValue(0)

        list = list_resources()
        self.combo = QtWidgets.QComboBox()
        self.combo.addItems(list)

        shbox.addWidget(self.start)
        shbox.addWidget(self.stop)
        shbox.addWidget(self.num)
        shbox.addWidget(self.combo)

        self.plot_widget = pg.PlotWidget()
        vbox.addWidget(self.plot_widget)

        start_button = QtWidgets.QPushButton("Start")
        vbox.addWidget(start_button)
        start_button.clicked.connect(self.plot)

        save_button = QtWidgets.QPushButton("Save")
        vbox.addWidget(save_button)
        save_button.clicked.connect(self.save)

    @Slot()
    def plot(self):
        self.plot_widget.clear()
        print(f"Work in progress, scan LED")

        diodeexperiment = DiodeExperiment()
        self.combo.setCurrentIndex(1)
        self.voltages, self.currents, self.v_errors, self.c_errors = diodeexperiment.scan(int(self.start.value()), int(self.stop.value()), int(self.num.value()), self.combo.currentText())

        self.plot_widget.plot(self.voltages, self.currents, symbol="o", symbolSize=5, pen=None)
        self.plot_widget.setLabel("left", "currents")
        self.plot_widget.setLabel("bottom", "voltages")

        # error_bars = pg.ErrorBarItem(x=self.voltages, y=self.currents, width=2 * np.array(self.v_errors), height=2 * np.array(self.c_errors))
        # self.plot_widget.addItem(error_bars)


    def save(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CSV files (*.csv)")


def main():
        app = QtWidgets.QApplication(sys.argv)
        ui = UserInterface()
        ui.plot()
        ui.show()
        sys.exit(app.exec())


if __name__ == "__main__":
    main()  