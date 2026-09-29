# 🛡️ AEGIS Intelligence v5.0

<p align="center">
  <a href="https://github.com/abidali72/-AEGIS-Intelligence-v5.0/actions/workflows/ci.yml">
    <img src="https://github.com/abidali72/-AEGIS-Intelligence-v5.0/actions/workflows/ci.yml/badge.svg" alt="CI Build Status">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-3776AB?style=flat&logo=python&logoColor=white" alt="Python Version">
  </a>
  <a href="https://pytorch.org/">
    <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white" alt="PyTorch">
  </a>
  <a href="https://opencv.org/">
    <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white" alt="OpenCV">
  </a>
  <a href="https://github.com/ultralytics/ultralytics">
    <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-FF6F00?style=flat&logo=ultralytics&logoColor=white" alt="YOLOv8">
  </a>
  <a href="https://flask.palletsprojects.com/">
    <img src="https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white" alt="Flask">
  </a>
  <a href="https://sqlite.org/">
    <img src="https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white" alt="SQLite">
  </a>
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style: Black">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>
  <a href="https://github.com/abidali72/-AEGIS-Intelligence-v5.0/stargazers">
    <img src="https://img.shields.io/github/stars/abidali72/-AEGIS-Intelligence-v5.0?style=social" alt="GitHub Stars">
  </a>
  <a href="https://github.com/abidali72/-AEGIS-Intelligence-v5.0/network/members">
    <img src="https://img.shields.io/github/forks/abidali72/-AEGIS-Intelligence-v5.0?style=social" alt="GitHub Forks">
  </a>
</p>

**Advanced Biometric & Neural Security Platform**

AEGIS Intelligence is a high-performance computer vision suite designed for real-time security monitoring, behavioral analysis, and automated threat detection. Leveraging custom-trained **YOLOv8** models, it provides a dual-interface command center for comprehensive environmental awareness.

---

## 🚀 Vision & Overview

In modern high-security environments, passive monitoring is no longer sufficient. **AEGIS Intelligence** transforms standard video feeds into proactive intelligence streams. It doesn't just "record"; it **understands**.

- **Detects** prohibited behaviors (e.g., indoor smoking) with sub-second latency.
- **Analyzes** biometric markers and subject metrics in real-time.
- **Alerts** security personnel through automated snapshots and neural notifications.
- **Archives** every significant event into an auditable, encrypted database.

---

## ✨ Key Features

### 🧠 Neural Engine
*   **Behavioral Detection**: Specialized YOLOv8 integration for detecting smoking and other anomalous activities.
*   **Biometric Estimation**: Real-time height estimation and motion state tracking for all detected subjects.
*   **Contextual Intelligence**: Analyzes the relationship between subjects and objects (e.g., mouth-zone tracking for smoking confirmation).

### 🖥️ Dual-Interface Command Center
*   **Desktop Dashboard**: A futuristic, glassmorphism-inspired UI built with `customtkinter` for local security stations.
*   **Web Dashboard**: A remote Flask-powered command center for browser-based monitoring from any device on the network.

### 📊 Security Pipeline
*   **Automated Event Logging**: Every detection is timestamped and stored in a local SQLite database.
*   **Incident Archives**: Built-in viewer for historical snapshots and alert logs.
*   **Live Diagnostics**: Real-time health monitoring of the AI inference pipeline.

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.9+ |
| **AI / Computer Vision** | OpenCV, PyTorch, Ultralytics YOLOv8 |
| **Desktop UI** | CustomTkinter, Pillow |
| **Web Interface** | Flask, HTML5, CSS3 |
| **Database** | SQLite3 |
| **Concurrency** | Multithreading (Inference/UI Separation) |

---

## 📦 Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.9+** and a working webcam or RTSP video feed.

### 2. Setup Environment
```bash
# Clone the repository
git clone https://github.com/abidali72/-AEGIS-Intelligence-v5.0.git
cd -AEGIS-Intelligence-v5.0

# Create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Neural Weights
Place your `yolov8n.pt` (or custom model) in the root directory.

---

## 🧪 Testing & Verification

Run the automated test suite to verify system integrity:
```bash
python -m unittest discover -s tests
```

---

## 🏃 Running AEGIS

### 🖥️ Option A: Desktop Command Center
Launch the primary GUI interface for local monitoring:
```bash
python app.py
```

### 🌐 Option B: Web Dashboard
Launch the web-based remote interface (Default: `http://127.0.0.1:5000`):
```bash
python web_app.py
```

---

## 📂 Project Architecture

*   `app.py`: Main entry point for the Desktop GUI application.
*   `web_app.py`: Flask application for the remote web dashboard.
*   `detector.py`: Core AI wrapper for YOLOv8 and computer vision logic.
*   `database.py`: Handles all SQLite operations and event persistence.
*   `notifier.py`: Background service for managing security alerts.
*   `tests/`: Comprehensive unit test suite.
*   `.github/`: CI workflows and issue/PR templates.
*   `captures/` / `archives/`: Directories where incident snapshots are stored.

---

## 📄 License & Credits
**AEGIS Intelligence** is developed under the MIT License.

---

<div align="center">
  <p><i>Empowering Security through Artificial Intelligence</i></p>
</div>
