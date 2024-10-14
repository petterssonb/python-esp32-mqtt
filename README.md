# Secure IoT Proof of Concept (PoC) using ESP32, Flask, MQTT, and Docker

## Overview

This repository contains the Proof of Concept (PoC) for a secure IoT solution. The PoC demonstrates secure communication between an ESP32 sensor, a Flask server running on a MacBook, and a Raspberry Pi hosting an MQTT broker inside a Docker container. The communication path is secured using a VPN and will later be upgraded to HTTPS.

This project was developed as part of a task to meet the requirements of the Cyber Resilience Act (CRA), ensuring a secure and resilient IoT architecture.

## System Architecture

The PoC includes the following components:

1. **ESP32**: A WiFi-enabled microcontroller that collects sensor data and sends it over HTTP (to be upgraded to HTTPS).
2. **Flask Server**: A Python Flask application running on a MacBook, acting as a local server to receive data from the ESP32.
3. **Raspberry Pi (RPI)**: A remote device hosting an MQTT broker inside a Docker container.
4. **Netbird VPN**: A secure VPN tunnel connecting the Flask server to the Raspberry Pi, ensuring secure transmission of MQTT messages.

### Communication Flow

1. **ESP32 -> Flask (MacBook)**:
   - ESP32 sends sensor data via HTTP (soon HTTPS) to the Flask server.
   - Security upgrade to HTTPS is planned to protect data in transit.
  
2. **Flask (MacBook) -> Raspberry Pi**:
   - Flask forwards the received data to the MQTT broker hosted on a Raspberry Pi over an MQTT protocol.
   - Communication between MacBook and Raspberry Pi is secured using the Netbird VPN solution.

3. **MQTT Broker (Raspberry Pi)**:
   - The Raspberry Pi hosts an MQTT broker inside a Docker container, which receives and processes the sensor data.

## Installation

### Prerequisites
- ESP32 (with required sensors)
- MacBook with Python installed
- Raspberry Pi (with Docker installed)
- Netbird VPN set up between the MacBook and Raspberry Pi

### Steps to Set Up

1. **ESP32 Configuration**:
   - Flash the ESP32 with the appropriate firmware to collect sensor data and send HTTP POST requests.
   
2. **Flask Server**:
   - Install required dependencies:
     ```bash
     pip install Flask
     ```
   - Run the Flask server on your MacBook:
     ```bash
     python app.py
     ```
   
3. **Raspberry Pi (MQTT broker)**:
   - Ensure Docker is installed and set up on the Raspberry Pi.
   - Use a Docker container to run the MQTT broker (e.g., Eclipse Mosquitto):
     ```bash
     docker run -d -p 1883:1883 -p 9001:9001 eclipse-mosquitto
     ```

4. **Netbird VPN Setup**:
   - Follow [Netbird](https://netbird.io/docs) documentation to establish a secure VPN tunnel between your MacBook and Raspberry Pi.
   - Once connected, the Raspberry Pi will securely receive MQTT messages.

## Upcoming Features

- **HTTPS Communication**:
  - The current implementation uses HTTP to transmit data between ESP32 and Flask. In line with the CRA requirements for secure communication, this will be upgraded to HTTPS.

- **Security Enhancements**:
  - Implement TLS/mTLS for securing the communication between devices.
  - Further refine the system's security features following Zero Trust principles.
  
## Security Planning and CRA Requirements

This project considers several key security elements to ensure compliance with the Cyber Resilience Act:

1. **Security-by-Design**:
   - The system is designed from the ground up with security in mind, using VPN to secure communication between devices and soon upgrading HTTP to HTTPS.
   - MQTT communication is restricted to authenticated clients.
   
2. **Updateability**:
   - Future plans include designing OTA (Over-the-Air) updates for the ESP32 to ensure that security patches can be easily applied.
   
3. **Vulnerability Management**:
   - A security monitoring system will be put in place to detect and report vulnerabilities in real-time.
   - Dockerized deployment of the MQTT broker allows quick updates and containerized security isolation.

## Potential Threats and Mitigation

- **Man-in-the-Middle (MITM) Attacks**:
  - Data between the ESP32 and Flask server will be protected using HTTPS to prevent MITM attacks.
  
- **Unauthorized Access**:
  - VPN ensures that the communication between Flask and Raspberry Pi is restricted to authenticated devices.
  
- **Data Tampering**:
  - MQTT broker messages will be secured through TLS to ensure data integrity during transmission.

## How the Design Meets CRA Requirements

The Cyber Resilience Act mandates strict security measures for IoT devices, and our design aligns with the act by:

1. **Implementing Secure Communication Paths**: Through HTTPS, TLS, and VPN, the solution ensures that data in transit is protected.
2. **Emphasizing Updateability and Maintenance**: Future updates, including security patches, are planned with OTA mechanisms and containerized MQTT brokers.
3. **Vulnerability Management**: Plans to integrate security monitoring and alerts to address potential vulnerabilities proactively.

## Conclusion

This PoC showcases a secure IoT solution using ESP32, Flask, MQTT, Docker, and VPN technologies. It provides a foundation for meeting the Cyber Resilience Act's security requirements, making it a viable candidate for transitioning into a production-ready system. Further security enhancements are planned, such as upgrading HTTP to HTTPS and implementing OTA updates for the ESP32.