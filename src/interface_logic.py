from PySide6 import QtWidgets

from main_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        self.buttons()

    def show(self):
        self.main_window.show()

    def buttons(self):
        self.ui.choose_files_btn.clicked.connect(self.open_files)

    def open_files(self):
        if any([self.ui.single_file_rbtn.isChecked(), self.ui.many_files_rbtn.isChecked()]):
            if self.ui.single_file_rbtn.isChecked():
                filepath: tuple = QtWidgets.QFileDialog.getOpenFileName()
                if filepath[0]:
                    self.ui.chosen_fiels_textEdit.clear()
                    self.ui.chosen_fiels_textEdit.setText(filepath[0])
                else:
                    self.ui.chosen_fiels_textEdit.clear()
                    self.ui.chosen_fiels_textEdit.setText("Вы не выбрали файл")
            elif self.ui.many_files_rbtn.isChecked():
                files: list = QtWidgets.QFileDialog.getOpenFileNames()[0]
                self.ui.chosen_fiels_textEdit.clear()
                output: str = ""
                for file in files:
                    output += file + "\n"
                self.ui.chosen_fiels_textEdit.setText(output)
        else:
            self.ui.chosen_fiels_textEdit.clear()
            self.ui.chosen_fiels_textEdit.setText("Выберите количество файлов для загрузки!")
