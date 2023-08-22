from Interface.UI import Fractals_Mainwindow as f
from PyQt6.QtWidgets import QApplication, QMainWindow

ui = f.Ui_MainWindow()
app = QApplication([])
window = QMainWindow()
ui.setupUi(window)
window.show()
app.exec()