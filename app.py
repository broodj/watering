import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class WateringApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Watering")

        button = QPushButton("Press me!")

        self.setCentralWidget(button)


def main():
    app = QApplication(sys.argv)
    window = WateringApplication()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()