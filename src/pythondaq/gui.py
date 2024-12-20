import sys
from pythondaq.diode_experiment import DiodeExperiment, list_resources
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
import pyqtgraph as pg
import numpy as np
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

class UserInterface(QtWidgets.QMainWindow):
    """Class that creates the interface for you experiment.

    Args:
        QtWidgets: Functions to make the interface with.
    """
    pass

    def __init__(self):
        """Create the interface with labels, spinboxes and the plot.
        """

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
        combolabel = QtWidgets.QLabel("Port")

        lhbox.addWidget(strlabel)
        lhbox.addWidget(stplabel)
        lhbox.addWidget(numlabel)
        lhbox.addWidget(combolabel)

        self.start = QtWidgets.QDoubleSpinBox()
        self.start.setMinimum(0)
        self.start.setValue(0)

        self.stop = QtWidgets.QDoubleSpinBox()
        self.stop.setMaximum(3.3)
        self.stop.setValue(0)

        self.num = QtWidgets.QSpinBox()
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
        """Creates the plot of your results with predetermined values for the experiment.
        """
        self.plot_widget.clear()

        diodeexperiment = DiodeExperiment()
        if self.start.value() > self.stop.value():
            print("Starting value can not be higher than the stop value.")
        elif self.num.value() == 0:
            print("You can not run this experiment zero times.")
        else:
            print(f"Work in progress, scan LED")
            self.voltages, self.currents, self.v_errors, self.c_errors = diodeexperiment.scan(int(self.start.value()), int(self.stop.value()), int(self.num.value()), self.combo.currentText())

            self.plot_widget.plot(self.voltages, self.currents, symbol="o", symbolSize=5, pen=None)
            self.plot_widget.setLabel("left", "currents (A)")
            self.plot_widget.setLabel("bottom", "voltages (V)")

            error_bars = pg.ErrorBarItem(x=np.array(self.voltages), y=np.array(self.currents), width=2 * np.array(self.v_errors), height=2 * np.array(self.c_errors))
            self.plot_widget.addItem(error_bars)
        
            diodeexperiment.close()

    def save(self):
        """Enables the user to save your results in a csv file with a chosen name.
        """
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CSV files (*.csv)")
        
        
def main():
    """Starts the interface.
    """
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()  