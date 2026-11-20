# Autonomous SecOps Incident Response Agent

> **An AI-Powered Tier-1 SOC Analyst for Real-Time IoT Intrusion Detection & Automated Threat Mitigation**

---

## 📌 Overview

Modern enterprise and IoT networks generate massive volumes of telemetry and security logs daily. Human security analysts frequently face **alert fatigue**—sifting through high-volume alarms while critical threats like DoS/DDoS floods, brute-force attempts, and port reconnaissance unfold in milliseconds.

This system provides an end-to-end autonomous **Security Operations Center (SOC) Incident Response Agent**:

1. **Perception Layer (ML Intrusion Detector):** A high-speed multi-class classifier trained on IoT network flow telemetry (83 features) to detect attack signatures in under 2ms.
2. **Cognitive Layer (Autonomous SOAR Agent):** An LLM-powered agent that triages alerts, computes threat severity and blast radius, executes automated mitigation tools (`block_ip`, `isolate_port`), and generates audit-ready post-mortem incident reports.
3. **Operations Console (Interactive Dashboard):** A real-time web console for security operators to monitor live traffic streams, simulate attacks, and supervise automated actions.

---

## 📊 Dataset Specification

* **Dataset:** RT-IoT2022 (Real-Time Internet of Things 2022)
* **Source:** [UCI Machine Learning Repository (Dataset ID: 942)](https://archive.ics.uci.edu/dataset/942/rt-iot2022)
* **Storage Location:** `data/RT_IOT2022.csv` (automatically fetched via `ucimlrepo` if absent)
* **Dimensions:** 123,117 network flow records across 83 numerical features.
* **Target Classes (12 Verified Types):**
  * **DoS / DDoS Attacks:** `DOS_SYN_Hping`, `DDOS_Slowloris`
  * **Reconnaissance & Port Scans:** `NMAP_UDP_SCAN`, `NMAP_XMAS_TREE_SCAN`, `NMAP_OS_DETECTION`, `NMAP_TCP_scan`, `NMAP_FIN_SCAN`
  * **Man-In-The-Middle & Brute Force:** `ARP_poisioning`, `Metasploit_Brute_Force_SSH`
  * **Normal Smart-Home Traffic:** `Thing_Speak`, `MQTT_Publish`, `Wipro_bulb`

---

## 🚀 Quickstart

### 1. Installation
Clone the repository and install required dependencies:
```bash
git clone https://github.com/<your-username>/SecOps_AI_Agent.git
cd SecOps_AI_Agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Verify Dataset Setup
The configuration script automatically resolves the local dataset or downloads it directly from UCI on first run:
```bash
python3 src/config.py
```


