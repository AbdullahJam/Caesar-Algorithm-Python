from PyQt5 import QtWidgets, QtCore
import sys

def caesar_cipher(text, shift):
    """Encrypts or decrypts a given text using the Caesar cipher algorithm."""
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create the widgets
        self.input_text = QtWidgets.QPlainTextEdit()
        self.output_text = QtWidgets.QPlainTextEdit()
        self.encrypt_button = QtWidgets.QPushButton("Encrypt")
        self.decrypt_button = QtWidgets.QPushButton("Decrypt")
        self.shift_label = QtWidgets.QLabel("Shift amount:")
        self.shift_spinbox = QtWidgets.QSpinBox()
        self.shift_spinbox.setMinimum(1)
        self.shift_spinbox.setMaximum(25)
        self.shift_spinbox.setValue(3)

        # Create the layout
        layout = QtWidgets.QGridLayout()
        layout.addWidget(QtWidgets.QLabel("Input text:"), 0, 0)
        layout.addWidget(self.input_text, 1, 0)
        layout.addWidget(QtWidgets.QLabel("Output text:"), 0, 1)
        layout.addWidget(self.output_text, 1, 1)
        layout.addWidget(self.shift_label, 2, 0)
        layout.addWidget(self.shift_spinbox, 2, 1)
        layout.addWidget(self.encrypt_button, 3, 0)
        layout.addWidget(self.decrypt_button, 3, 1)
        self.setLayout(layout)

        # Connect the signals and slots
        self.encrypt_button.clicked.connect(self.encrypt_text)
        self.decrypt_button.clicked.connect(self.decrypt_text)

    def encrypt_text(self):
        text = self.input_text.toPlainText()
        shift = self.shift_spinbox.value()
        encrypted_text = caesar_cipher(text, shift)
        self.output_text.setPlainText(encrypted_text)

    def decrypt_text(self):
        text = self.input_text.toPlainText()
        shift = self.shift_spinbox.value()
        decrypted_text = caesar_cipher(text, -shift)
        self.output_text.setPlainText(decrypted_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    window.geometry("600x600")
    sys.exit(app.exec_())