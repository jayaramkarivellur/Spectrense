# 🛰️ SpectrUS VNA – Homemade 6 GHz Vector Network Analyzer

<img src="images/spectrus_logo.png" alt="SpectrUS Logo" width="200" />

**SpectrUS VNA** is a compact, home-built vector network analyzer designed for RF measurements up to **6 GHz**. It offers affordable and extensible S-parameter testing for engineers, researchers, and students—entirely open-source and built from the ground up.

---

## ⚡ Project Highlights

- 📊 Measures **S11** and **S21** (reflection and transmission)
- 🌐 Frequency range: **10 MHz – 6 GHz**
- 🧩 Modular RF design using off-the-shelf components
- 💻 Python-based GUI with real-time visualization
- 🔧 Open-source hardware + firmware = total customization

---

## 🔩 Hardware Overview

- Directional couplers, RF switches, mixers, and PLL synthesizers
- Microcontroller: STM32 / RP2040 / ESP32
- High-speed ADC for signal capture
- USB-C / UART for host control
- Shielded RF board layout for performance

🛠️ Full schematics, BOM, and Gerber files in `hardware/`

---

## 💻 Software Features

- 🖥️ Frequency sweep & resolution bandwidth control
- 📐 Smith Chart and log magnitude plots
- ⚙️ Full calibration routine: **Open**, **Short**, **Load**, **Thru**
- 🧪 Save S-parameter files in Touchstone format
- 🐍 Python GUI (Tkinter or PyQt) + CLI mode

---

## 📂 Folder Structure

```bash
spectrus-vna/
├── hardware/           # Schematics and PCB layouts
├── firmware/           # MCU code (e.g., STM32)
├── software/           # Python GUI and interface logic
├── calibration/        # Tools and sample cal files
├── images/             # Logos, screenshots, diagrams
└── README.md
