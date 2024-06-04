from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

from main_ui import Ui_MainWindow
from start_calculating_logic import Calculator


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.main_window: QtWidgets.QMainWindow = QtWidgets.QMainWindow()
        self.icon_path: str = r'C:\Users\1234x\PycharmProjects\biolog\src\interface_icon.png'
        self.app_icon: QIcon = QIcon(self.icon_path)
        self.main_window.setWindowIcon(self.app_icon)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        self.buttons()

    def show(self):
        self.main_window.show()

    def buttons(self):
        self.ui.choose_files_btn.clicked.connect(self.open_files)
        self.ui.start_calculating_btn.clicked.connect(self.calculate)

    def open_files(self):
        files: list = QtWidgets.QFileDialog.getOpenFileNames()[0]
        self.ui.chosen_fiels_textEdit.clear()
        output: str = "\n".join(files)
        self.ui.chosen_fiels_textEdit.setText(output)

    def calculate(self):
        if any([self.ui.single_file_rbtn.isChecked(), self.ui.many_files_rbtn.isChecked()]):
            calculator: Calculator = Calculator()
            files: list = self.ui.chosen_fiels_textEdit.toPlainText().split("\n")
            try:
                for file in files:
                    if not(file.endswith(".xls")) and not(file.endswith(".xlsx")):
                        raise BufferError()

                if self.ui.single_file_rbtn.isChecked():
                    calculator.calculate_files_for_one(files)
                elif self.ui.many_files_rbtn.isChecked():
                    calculator.calculate_files_for_many(files)

                QtWidgets.QMessageBox.information(self,
                                                  "Завершено",
                                                  "Работа завершена, проверьте директорию с первым файлом в списке")
                self.ui.chosen_fiels_textEdit.clear()
            except BufferError:
                QtWidgets.QMessageBox.warning(self,
                                              "Ошибка",
                                              "Выбирите файлы с расширениями .xls или .xlsx")

        else:
            self.ui.chosen_fiels_textEdit.clear()
            self.ui.chosen_fiels_textEdit.setText("Выберите количество файлов для вывода!")