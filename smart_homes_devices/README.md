# Smart Home Devices (Multiple Inheritance Project)

This project demonstrates how **multiple inheritance** can be used to 
combine different features (power, network, and device properties) into a 
single smart home device system using Python.

---

## 💡 Concepts Demonstrated

* Classes and Objects
* Multiple Inheritance (The core focus)
* Attribute Initialization (__init__)
* Method Implementation
* Real-world Object-Oriented Programming (OOP) modeling

---

## ✨ Features

The resulting SmartHomeDevice class supports the following 
functionalities:

* Turn a device **ON** or **OFF**
* Connect the device to a **WiFi** network
* Display full device **information** (ID, status, network details, etc.)

---

## 📁 Class Structure

The system is built upon three main classes that use multiple inheritance:

| Class | Responsibility |
| :--- | :--- |
| PowerFeatures | Handles power status (ON/OFF) and power source (e.g., 
Battery, Wall) |
| NetworkFeatures | Handles network details like the WiFi name and IP 
address |
| SmartHomeDevice | Combines both parent classes and adds unique 
device-specific details (e.g., Device ID) |

---

## ▶️ How to Run

1.  **Clone the project** repository to your local machine.
2.  **Open the file** (smart_home.py) in your Python environment.
3.  **Execute the script** from your terminal:

```bash
python smart_home.py
