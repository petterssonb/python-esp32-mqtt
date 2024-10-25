# Secure IoT Proof of Concept (PoC) using ESP32, BLE, Flask, MQTT, and Docker

Click on [Powerpoint](content/IoT-PoC.pptx) and then **view raw** to download it

## Screenshots

Click [here](content/README.md) to view the screenshots of the program running. 

### Project Overview

This repository presents a Proof of Concept (PoC) for a secure IoT solution that enables secure communication between various IoT components. This setup demonstrates an architecture that is scalable, resilient, and compliant with the **Cyber Resilience Act (CRA)**. The PoC showcases the integration of **ESP32**, **BLE**, **Flask**, **MQTT**, **Docker**, and **Netbird VPN** for secure data transmission and management.

### Objectives and Compliance with Cyber Resilience Act (CRA)

The project is designed to showcase:
1. **End-to-End Security**: Secure communication from data source (ESP32) to data endpoint (MQTT broker on Raspberry Pi).
2. **Robustness and Resilience**: Adherence to CRA requirements, including:
   - **Security-by-Design**: Secure architecture with encryption, VPN, and Zero Trust.
   - **Updateability**: Plans for OTA updates and security patching.
   - **Vulnerability Management**: Regular assessment of vulnerabilities and integration of necessary mitigations.


## System Architecture

The architecture integrates secure, multi-layered communication from sensor devices to the cloud, demonstrating scalable and resilient communication flows.

### Architecture Components

1. **ESP32**: A WiFi-enabled microcontroller with attached sensors (e.g., temperature, humidity) that transmits data via **Bluetooth Low Energy (BLE)**.
2. **BLE Server (MacBook)**: Acts as an intermediary, receiving BLE data from ESP32 and forwarding it to the Flask server over HTTPS.
3. **Flask Server (MacBook)**: A Python-based server receiving BLE data, which forwards it securely to the MQTT broker.
4. **Raspberry Pi (MQTT Broker)**: Hosts an MQTT broker in a Docker container, processing and storing received data.
5. **Netbird VPN**: Establishes a secure, encrypted VPN tunnel, ensuring confidentiality and integrity between the Flask server and the MQTT broker on Raspberry Pi.

### Communication Flow Overview

1. **ESP32 -> BLE Server (MacBook)**: Data is transmitted via BLE.
2. **BLE Server -> Flask Server**: The BLE server forwards data securely to the Flask server over HTTPS.
3. **Flask Server -> Raspberry Pi**: Data is sent from the Flask server to the MQTT broker over an encrypted VPN (Netbird), ensuring secure MQTT message delivery.

### Communication Protocol Summary

| Communication Path          | Protocol   | Security Measures                  |
|-----------------------------|------------|------------------------------------|
| ESP32 -> BLE Server         | BLE        | Secure pairing and authentication  |
| BLE Server -> Flask Server  | HTTPS      | TLS for encrypted transmission     |
| Flask Server -> Raspberry Pi | MQTT + VPN | Encrypted VPN tunnel              |


## Security Implementation

### Security Mechanisms

1. **HTTPS Communication**: TLS encryption protects data in transit between the BLE server and the Flask server, mitigating **Man-in-the-Middle (MITM)** attacks.
2. **Zero Trust Model**: Authentication and minimum privilege principles restrict access, ensuring each device and service is granted only the necessary permissions.
3. **VPN Security**: Netbird VPN encrypts data between the Flask server and the MQTT broker, ensuring secure, authenticated communication.

### Threat Mitigation Summary

- **MITM Attacks**: HTTPS and VPN encryption protect against interception and modification.
- **Unauthorized Access**: VPN and certificate-based authentication restrict network access to authorized devices.
- **Data Tampering**: VPN encryption and Zero Trust principles preserve data integrity in transit.

---

## Compliance with Cyber Resilience Act (CRA) Requirements

### Security-by-Design

The solution has integrated security measures from the outset:
- **Encrypted Communication**: TLS and VPN encryption are implemented for secure data transmission.
- **Access Control and Authentication**: Zero Trust principles enforce authentication and minimum access rights.
- **Isolation and Containerization**: Docker containers isolate the MQTT broker, ensuring modular and secure deployment on the Raspberry Pi.

### Updateability

Future updates are planned to include:
- **Over-the-Air (OTA) Updates** for ESP32, enabling remote firmware updates for security patching.
- **Automated Software Updates** for Docker containers on the Raspberry Pi, ensuring that the MQTT broker and other dependencies are regularly updated.

### Vulnerability Management

- **Regular Vulnerability Scanning**: Security scanning tools will be integrated for ESP32, Flask, and Docker components to identify potential vulnerabilities.
- **Logging and Monitoring**: Plans for integrating logging and monitoring on the Raspberry Pi to detect anomalies and potential attacks.
- **Incident Response Plan**: Developing a plan for incident response to ensure prompt action and containment of vulnerabilities, as required by the CRA.

---

## Installation

### Prerequisites

Ensure that the following components are available:
- **ESP32**: Configured with necessary sensors.
- **MacBook**: Capable of running Python, BLE support, and Flask.
- **Raspberry Pi**: Docker-installed device for hosting MQTT broker.
- **Netbird VPN**: Configured and set up between MacBook and Raspberry Pi for secure communication.

### Cloning the Repository with Submodules

This repository includes a submodule for **arduino-esp32** under the `lib` directory, required for Bluetooth services. To clone the repository with the submodule:

1. **Clone the repository with submodules**:
   ```bash
   git clone --recurse-submodules https://github.com/yourusername/python-esp32-mqtt.git
   ```

   - If you've already cloned the repository without submodules, initialize and update the submodule separately:
     ```bash
     git submodule update --init --recursive
     ```

2. **Navigate to the project directory**:
   ```bash
   cd python-esp32-mqtt
   ```

### Step-by-Step Setup

1. **ESP32 Setup**:
   - Flash the ESP32 firmware to collect sensor data and send it over BLE.
```bash
   pio run
   ```

```bash
   pio run --target upload
   ```

  - View the serial monitor

```bash
   pio device monitor
   ```

2. **BLE Server (MacBook)**:
   - Install dependencies:
     ```bash
     pip install Flask bleak requests
     ```
   - Run the BLE server to receive and forward BLE data to the Flask server:
     ```bash
     python bleServer.py
     ```

3. **Flask Server (MacBook)**:
   - Configure and start the Flask server:
     ```bash
     python server.py
     ```

4. **MQTT Broker Setup (Raspberry Pi)**:
   - Set up and run the MQTT broker in a Docker container:
     ```bash
     docker run -d -p 1883:1883 -p 9001:9001 eclipse-mosquitto
     ```

5. **Netbird VPN**:
   - Configure a secure VPN tunnel between MacBook and Raspberry Pi.

---

## Future Enhancements and Compliance Improvements

1. **Enhanced Security Measures**:
   - **Device Authentication**: Introduce certificate-based device authentication for ESP32, enhancing identity verification.
   - **Intrusion Detection System (IDS)**: Integrate IDS on Raspberry Pi for detecting unauthorized access attempts.

2. **Monitoring and Logging**:
   - Implement logging for each component to capture communication flows and detect anomalies.
   - Add centralized logging and monitoring for easier tracking of security incidents.

3. **Extended CRA Compliance**:
   - **Comprehensive Incident Response Protocol**: Define and document a protocol aligned with CRA standards to address potential vulnerabilities.
   - **Lifecycle Management**: Regularly update firmware, software, and dependencies for ongoing security compliance.

---

## Conclusion

This PoC showcases a secure IoT solution that aligns with Cyber Resilience Act requirements. By integrating **ESP32**, **BLE**, **Flask**, **MQTT**, **Docker**, and **Netbird VPN**, the architecture supports secure, resilient data communication and aligns with CRA requirements through security-by-design, updatability, and vulnerability management. Future enhancements will continue to improve compliance, security monitoring, and incident response, making this solution a robust candidate for real-world IoT deployment.