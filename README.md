⚡ Tesla AI Energy Dashboard

An AI-powered real-time energy monitoring system built using Python, PyQt5, Matplotlib, and Machine Learning.

This project simulates (or connects to) a smart energy harvesting footwear system that generates voltage from walking steps and predicts future energy generation using AI.

🚀 Features

🔐 Secure Login System

📊 Real-Time Voltage Graph

👣 Step Counter (Voltage-Based Detection)

🔋 Live Battery Charging Animation

🤖 AI Energy Prediction (Linear Regression)

💾 Automatic CSV Data Logging

🌙 Modern Dark-Themed UI

🧠 How It Works

Voltage is generated from energy harvesting footwear (simulated using random values or real Arduino input).

If voltage crosses a threshold, a step is detected.

Voltage values are plotted in real-time.

Total energy is calculated from voltage data.

A Machine Learning model predicts the next energy output.

All data is saved into a CSV file for analysis.

🛠 Technologies Used

Python 3

PyQt5 (GUI Framework)

Matplotlib (Live Graph Plotting)

NumPy & Pandas

Scikit-learn (Linear Regression Model)

CSV File Handling

📂 Project Structure
tesla-ai-energy-dashboard/
│
├── main.py
├── energy_data.csv
├── README.md
💻 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/tesla-ai-energy-dashboard.git
cd tesla-ai-energy-dashboard
2️⃣ Install Dependencies
pip install pyqt5 matplotlib numpy pandas scikit-learn
3️⃣ Run the Application
python main.py
🔑 Default Login Credentials
Username: admin
Password: 1234
📊 Dashboard Preview
4
🤖 AI Prediction Model

The system uses Linear Regression to:

Analyze historical energy values

Train on collected data

Predict next energy output

Future upgrade ideas:

LSTM for time-series prediction

Random Forest Regression

Real IoT integration
