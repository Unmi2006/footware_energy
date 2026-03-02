import sys
import random
import csv
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox,
    QProgressBar, QHBoxLayout
)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


# ================= LOGIN =================

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tesla Energy Login")
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #0d0d0d;")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        logo = QLabel("⚡")
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet("font-size: 60px; color: #00f2ff;")
        layout.addWidget(logo)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.username.setStyleSheet(input_style())
        layout.addWidget(self.username)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet(input_style())
        layout.addWidget(self.password)

        btn = QPushButton("Login")
        btn.setStyleSheet(button_style())
        btn.clicked.connect(self.check_login)
        layout.addWidget(btn)

        self.setLayout(layout)

    def check_login(self):
        if self.username.text() == "admin" and self.password.text() == "1234":
            self.dashboard = Dashboard()
            self.dashboard.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Invalid Credentials")


# ================= DASHBOARD =================

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("⚡ Tesla AI Energy Dashboard")
        self.setGeometry(200, 50, 1100, 750)
        self.setStyleSheet("background-color: #0f0f0f; color: white;")

        self.steps = 0
        self.battery = 0
        self.voltages = []
        self.times = []
        self.energy_values = []

        layout = QVBoxLayout()

        title = QLabel("TESLA AI ENERGY MONITOR")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        info_layout = QHBoxLayout()

        self.step_label = QLabel("Steps: 0")
        self.energy_label = QLabel("Energy: 0 mWh")
        self.prediction_label = QLabel("Predicted Next Energy: --")

        info_layout.addWidget(self.step_label)
        info_layout.addWidget(self.energy_label)
        info_layout.addWidget(self.prediction_label)

        layout.addLayout(info_layout)

        # Battery
        self.battery_bar = QProgressBar()
        self.battery_bar.setMaximum(100)
        layout.addWidget(self.battery_bar)

        # Graph Setup
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(300)

    def update_data(self):
        voltage = random.uniform(0.2, 2.5)

        current_time = datetime.now().strftime("%H:%M:%S")

        if voltage > 1.5:
            self.steps += 1

        self.voltages.append(voltage)
        self.times.append(current_time)

        if len(self.voltages) > 50:
            self.voltages.pop(0)
            self.times.pop(0)

        energy = sum(self.voltages) * 0.1
        self.energy_values.append(energy)

        # Smooth Graph (no clear flicker)
        self.ax.cla()
        self.ax.plot(self.times, self.voltages, color="cyan")
        self.ax.set_facecolor("#0f0f0f")
        self.ax.set_title("Voltage vs Time", color="white")
        self.ax.set_ylabel("Voltage (V)")
        self.ax.set_xlabel("Time")
        self.ax.tick_params(colors='white')
        self.ax.tick_params(axis='x', rotation=45)
        self.canvas.draw()

        self.step_label.setText(f"Steps: {self.steps}")
        self.energy_label.setText(f"Energy: {energy:.2f} mWh")

        # Battery Animation
        self.battery += voltage * 0.4
        if self.battery > 100:
            self.battery = 100

        self.battery_bar.setValue(int(self.battery))

        # AI Prediction
        if len(self.energy_values) > 5:
            X = np.arange(len(self.energy_values)).reshape(-1, 1)
            y = np.array(self.energy_values)

            model = LinearRegression()
            model.fit(X, y)

            next_index = np.array([[len(self.energy_values)]])
            predicted = model.predict(next_index)[0]

            self.prediction_label.setText(
                f"Predicted Next Energy: {predicted:.2f} mWh"
            )

        # Save CSV
        with open("energy_data.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), voltage, self.steps])


# ================= STYLES =================

def input_style():
    return """
        QLineEdit {
            background-color: #262626;
            border-radius: 10px;
            padding: 10px;
            color: white;
        }
        QLineEdit:focus {
            border: 1px solid #00f2ff;
        }
    """

def button_style():
    return """
        QPushButton {
            background-color: #00f2ff;
            border-radius: 12px;
            padding: 10px;
            font-weight: bold;
            color: black;
        }
        QPushButton:hover {
            background-color: #00c3cc;
        }
    """


# ================= RUN =================

app = QApplication(sys.argv)
login = LoginWindow()
login.show()
sys.exit(app.exec_())