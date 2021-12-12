"""
Main Application python code

Author: Omar Abdelakher Hammad Mohamed
Last Edit: Dec 12, 2021
"""
from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys

# Matplotlib for plotting the function
import matplotlib
matplotlib.use('Qt5Agg')

# Configure matplotlib for integration with PyQt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    '''
    Class canvas for the Matplotlib figure canvas
    '''
    def __init__(self, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Function Plotter - Master Micro Demo")

        # Create figure canvas and add it to the main screen
        self.figure = MplCanvas()
        self.canvasLayout.addWidget(self.figure)

        # Add signal events
        self.plotBtn.clicked.connect(self.plot_fun)

    def plot_fun(self):
        # Read the user input
        fun = self.functionEdit.text()

        minVal = self.minVal.value()
        maxVal = self.maxVal.value()

        # Replace ^ with ** (python syntax)
        fun = fun.replace('^', '**')

        # Create the plot values
        x_vals = []
        y_vals = []
        for x in range(minVal, maxVal+1):
            # Try and check for the user input
            try:
                y = eval(fun)
            except NameError:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)

                msg.setText("Unknown variable entered. Make sure to only use 'x' as the equation variable")
                msg.setWindowTitle("Error: NameError")

                msg.exec_()
                return
            except TypeError:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)

                msg.setText("Error in the function. Did you forget to add an operator before a paranthesis?")
                msg.setWindowTitle("Error: NameError")

                msg.exec_()
                return
            except SyntaxError:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)

                msg.setText("Error in the function. Make sure that all operators are in place")
                msg.setWindowTitle("Error: NameError")

                msg.exec_()
                return
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)

                msg.setText("Error in the function. Please make sure it is written correctly")
                msg.setWindowTitle("Error: NameError")

                msg.exec_()
                return

            x_vals.append(x)
            y_vals.append(y)

        # Plot the function - delete old figure first
        self.canvasLayout.removeWidget(self.figure)
        self.figure.deleteLater()
        self.figure.setParent(None)

        # Add the new figure and plot the results
        self.figure = MplCanvas()
        self.canvasLayout.addWidget(self.figure)

        self.figure.axes.plot(x_vals,y_vals)
        self.figure.draw()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())