from PySide6.QtWidgets import (QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QLabel)
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl, Qt
import sys

class kalokohanwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("kalokohan")
        self.resize(600,400)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.miss_mo_label = QLabel("miss mo??")
        self.miss_mo_label.setStyleSheet("font-size: 70; padding: 0px; color: white;; margijn: opx;")
        self.miss_mo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.miss_mo_label)
        
        self.oo_button = QPushButton("OO")
        self.oo_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: blask;
                font-size: 30px:
                padding: 40px;
                border: none;
            }
            QPushButton:hover {
                background_color:: darkred;
            }
        """)
        layout.addWidget(self.oo_button)

        self.oo_button.clicked.connect(self.play_video)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setStyleSheet("""
            QMainWindow {
                background-image: url('sad.jpg')
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
            }
            QPushButton {
                background-image: none;
            }
        """)
        self.setCentralWidget(central_widget)

    def play_video(self):
        self.video_widget = QVideoWidget()
        self.player = QMediaPlayer()

        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        video_path = QUrl.fromLocalFile("video.mp4")
        self.player.setSource(video_path)
        self.player.setVideoOutput(self.video_widget)

        self.video_window = QMainWindow(self)
        self.video_window.setWindowTitle("Miss ka baa?")
        self.video_window.setCentralWidget(self.video_widget)
        self.video_window.resize(700, 400)

        self.video_window.show()
        self.player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = kalokohanwindow()
    window.show()
    sys.exit(app.exec())


