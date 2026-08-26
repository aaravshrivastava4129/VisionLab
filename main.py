import sys
import cv2

from PySide6.QtCore import QTimer, Qt, QEvent, QThread
from PySide6.QtGui import QImage, QPixmap, QPainter, QPainterPath
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QComboBox,
    QMessageBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.camera = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateFrame)

        self.setWindowTitle("VisionLab")
        self.resize(1920, 1040)

        self.cameraLabel = QLabel("Camera is off")
        self.cameraLabel.setObjectName("cameraLabel")
        self.cameraLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cameraLabel.setContentsMargins(0, 0, 0, 0)
        self.cameraLabel.setScaledContents(False)

        self.frame_holder = QWidget()
        self.frame_holder.setObjectName("frame_holder")


        self.headingLabel = QLabel("VisionLab")
        self.headingLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.headingLabel.setObjectName("headingLabel")

        self.compVisionLabel = QLabel("Computer Vision")
        self.compVisionLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.compVisionLabel.setObjectName("compVisionLabel")
        
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

        
        main_layout.addWidget(self.frame_holder, stretch=68)
        main_layout.addWidget(self.side_panel, stretch=32)

        frame_layout = QVBoxLayout(self.frame_holder)

        frame_layout.addWidget(self.cameraLabel, stretch=1)

        
        side_layout = QVBoxLayout(self.side_panel)
        side_layout.setContentsMargins(20, 15, 20, 30)
        side_layout.setSpacing(0)

        side_layout.addWidget(self.headingLabel)
        side_layout.addWidget(self.compVisionLabel)
        side_layout.addWidget(self.modeBox)
        side_layout.addStretch(1)
        side_layout.addWidget(self.startBtn)
        side_layout.addWidget(self.stopBtn)
        

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self._is_ready = False

    def start_camera(self):

        self.cameraLabel.setText("Camera is starting...")
        self.cameraLabel.setStyleSheet("color: #FF3366; font-weight: bold;")
        self.startBtn.hide()
        self.stopBtn.show()

        QApplication.processEvents()

        if not self.camera.isOpened():
            self.camera.open(0)

        self.timer.start(1) #CHANGE TO 33 BEFORE FINALLY MAKING IT PUBLIC

    def stop_camera(self):
        self.timer.stop()
        self.camera.release()
        self.cameraLabel.setText("Camera is off")
        self.cameraLabel.setStyleSheet("color: #FF3366; font-weight: bold;")
        self.startBtn.show()
        self.stopBtn.hide()
    
    def updateFrame(self):

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
            QImage.Format_RGB888
        )

        pixmap = QPixmap.fromImage(image)

        scaled_pixmap = pixmap.scaled(
            self.cameraLabel.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
            Qt.AlignmentFlag.AlignCenter
        )

        rounded_pixmap = QPixmap(scaled_pixmap.size())
        rounded_pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(0, 0, scaled_pixmap.width(), scaled_pixmap.height(), 10, 10)
        
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, scaled_pixmap)
        painter.end()

        self.cameraLabel.setPixmap(rounded_pixmap)
        self.cameraLabel.setContentsMargins(0, 0, 0, 0)


    def showEvent(self, event):
        super().showEvent(event)
        self._is_ready = True

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if hasattr(self, '_is_ready') and self._is_ready:
                if not self.isMinimized() or self.isMaximized():
                    self._is_ready = False
                    QMessageBox.warning(self, "Notice", "Sorry, this programme doesn't support changing the layout size.")
                    self.showMaximized()
                    event.accept()
                    self._is_ready = True
                    return
        super().changeEvent(event)
        

    def closeEvent(self, event):
        self.timer.stop()
        self.camera.release()
        event.accept()
        
with open("style.qss", "r") as file:
    stylesheet = file.read()

app = QApplication(sys.argv)
app.setStyleSheet(stylesheet)

window = MainWindow()
window.showMaximized()

sys.exit(app.exec())