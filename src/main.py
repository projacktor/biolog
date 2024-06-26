from PySide6 import QtWidgets
from interface_logic import MainWindow


def main():
    import sys
    app: QtWidgets.QApplication() = QtWidgets.QApplication(sys.argv)
    application = MainWindow()
    app.setWindowIcon(application.app_icon)
    application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
