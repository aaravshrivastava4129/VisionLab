import sys
import cv2

from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QComboBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.camera = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateFrame)

        self.setWindowTitle("VisionLab")
        self.resize(900, 600)

        self.cameraLabel = QLabel("Camera is off")
        self.cameraLabel.setObjectName("cameraLabel")
        self.cameraLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cameraLabel.setScaledContents(False)

        self.headingLabel = QLabel("VisionLab")
        self.headingLabel.setObjectName("headingLabel")

        self.modeBox = QComboBox()
        self.modeBox.setObjectName("modeBox")
        self.modeBox.addItem("Normal")
        self.modeBox.addItem("Grayscale")
        self.modeBox.addItem("Edges")

        self.startBtn = QPushButton("START CAMERA")
        self.startBtn.setObjectName("startBtn")
        self.startBtn.clicked.connect(self.start_camera)

        self.stopBtn = QPushButton("STOP CAMERA")
        self.stopBtn.setObjectName("stopBtn")
        self.stopBtn.clicked.connect(self.stop_camera)
        self.stopBtn.hide()

        self.side_panel = QWidget()
        self.side_panel.setObjectName("sidePanel")

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        main_layout.addWidget(self.cameraLabel, stretch=1)
        main_layout.addWidget(self.side_panel)

        side_layout = QVBoxLayout(self.side_panel)
        side_layout.setContentsMargins(20, 30, 20, 30)
        side_layout.setSpacing(15)

        side_layout.addWidget(self.headingLabel)
        side_layout.addWidget(self.modeBox)
        side_layout.addWidget(self.startBtn)
        side_layout.addWidget(self.stopBtn)

        side_layout.addStretch(1)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        def start_camera(self):

            self.cameraLabel.setText("Camera is starting...")
            self.cameraLabel.setStyleSheet("color: #FF3366; font-weight: bold;")
            self.startBtn.hide()
            self.stopBtn.show()

            QApplication.processEvents()

            if not self.camera.isOpened():
                self.camera.open(0)

            self.timer.start(1) #Gives Frames 33 is for 30FPS

        def stop_camera(self):
            self.timer.stop()
            self.camera.release()
            self.cameraLabel.setText("Camera is off")
            self.cameraLabel.setStyleSheet("color: #FF3366; font-weight: bold;")
            self.startBtn.show()
            self.stopBtn.hide()

        def update_frame(self):

            mode = self.modeBox.currentText()

            success, frame = self.camera.read()

            if not success:
                return

            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            if mode == "Normal":
                pass
            elif mode == "Grayscale":
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
            elif mode == "Edges":
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                frame = cv2.Canny(frame, 100, 200)
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)

            self.display_image(frame)

        def display_image(self, frame):
            height, width, channels = frame.shape
            bytes_per_line = channels * width

            image = QImage(
                frame.data,
                width,
                height,
                bytes_per_line,
                QImage.Formate_RGB888
            )

            pixmap = QPixmap.fromImage(image)

            scaled_pixmap = pixmap.scaled(
                self.cameraLabel.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
                Qt.AlignmentFlag.AlignCenter
            )

            self.cameraLabel.setPixmap(scaled_pixmap)
            self.cameraLabel.setContentsMarigns(0, 0, 0, 0)

        def closeEvent(self, event):
            self.timer.stop()
            self.camera.release()
            event.accept()

with open("style.qss", "r") as file:
    stylesheet = file.read()

app = QApplication(sys.argv)
app.setStyleSheet(stylesheet)

window = MainWindow()
window.show()
