# 🛡 AI Network Intrusion Detection System (IDS)

A real-time cybersecurity dashboard developed for the CodeAlpha Cyber Security Internship.

This project monitors live network traffic, detects suspicious activities, generates real-time alerts, and visualizes intrusion attempts using an interactive dashboard.

---

## 🚀 Features

- Real-time packet monitoring
- Port scan detection
- SYN flood detection
- Ping flood detection
- Suspicious traffic alerts
- Live dashboard analytics
- Threat severity classification
- CSV alert logging
- Real-time chart updates

---

## 🛠 Technologies Used

- Python
- Flask
- Flask-SocketIO
- Scapy
- HTML
- CSS
- JavaScript
- Chart.js

---

## 📂 Project Structure

```bash
CodeAlpha_NetworkIDS/
│
├── app.py
├── detector.py
├── alerts.csv
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

## 🧪 Testing

Generate traffic using:

```bash
ping google.com -t
```

The dashboard will start detecting and displaying live threats.

---

## 👨‍💻 Author

Naveen R  
Cyber Security Intern — CodeAlpha
