import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit
from PyQt6.QtGui import QPixmap

class BeetlejuiceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Beetlejuice Summoning")
        
        self.label = QLabel("Welcome to the Beetlejuice summoning script!\nTo summon Beetlejuice, say his name three times.")
        self.entry = QLineEdit()
        self.submit_button = QPushButton("Summon Beetlejuice")
        self.result_label = QLabel("")
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.result_label)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        self.summon_count = 0
        self.submit_button.clicked.connect(self.summon_beetlejuice)
        
    def summon_beetlejuice(self):
        user_input = self.entry.text().strip().lower()
        if user_input == "beetlejuice":
            self.summon_count += 1
            self.result_label.setText(f"Beetlejuice! ({self.summon_count}/3)")
            if self.summon_count == 3:
                self.result_label.setText("Beetlejuice has been summoned successfully!")
                self.show_beetlejuice_face()
        else:
            self.result_label.setText("That's not Beetlejuice's name! Try again.")
        self.entry.clear()
    
    def show_beetlejuice_face(self):
        self.beetlejuice_window = QWidget()
        self.beetlejuice_window.setWindowTitle("Beetlejuice")
        
        pixmap = QPixmap("beetlejuice.jpg")
        label = QLabel(self.beetlejuice_window)
        label.setPixmap(pixmap.scaled(512, 512, aspectRatioMode='KeepAspectRatio'))
        
        layout = QVBoxLayout(self.beetlejuice_window)
        layout.addWidget(label)
        
        self.beetlejuice_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BeetlejuiceApp()
    window.show()
    sys.exit(app.exec())
