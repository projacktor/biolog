from PySide6 import QtWidgets, QtGui
from interface_logic import MainWindow


def main():
    import sys
    app: QtWidgets.QApplication() = QtWidgets.QApplication(sys.argv)
    application = MainWindow()
    app.setWindowIcon(QtGui.QIcon(application.icon_path))
    application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
