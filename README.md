# Network Checksum Analysis

This project demonstrates checksum validation and network packet analysis using Wireshark and the Scapy Python library. The experiment verifies data integrity by validating checksums using three different methods.

---

## 📌 Objectives

- Capture live network traffic
- Validate checksums using Wireshark
- Perform manual IPv4 checksum calculation
- Automate checksum validation using Scapy
- Analyze packets for multiple protocols

---

## 🧰 Tools & Technologies Used

- Wireshark
- Python
- Scapy Library
- VS Code

---

## 📂 Project Structure
network-checksum-analysis
│
├── checksum_validation.py
├── sample_capture.pcap
└── report.pdf


---

## 🔍 Methods Implemented

### Method 1 – Wireshark Validation
Wireshark's built-in checksum validation feature is used to verify packet integrity by checking TCP, UDP, IP, and ICMP checksums.

---

### Method 2 – Manual Checksum Calculation
IPv4 header checksum is manually calculated by:
- Extracting header fields
- Converting fields into 16-bit words
- Performing one's complement addition
- Comparing calculated checksum with Wireshark value

---

### Method 3 – Scapy Automation
Python script uses Scapy to:
- Read packets from PCAP file
- Extract checksum values
- Recalculate checksums
- Compare original and computed results

---

## ▶️ How To Run The Code

1. Install Scapy:
2. Place PCAP file in project folder.
3. Run script:

