# Packet Sniffer Tool

## Description

This is a simple packet sniffer tool built using Python and the Scapy library. The tool captures network packets on a specified network interface and displays relevant information such as source and destination IP addresses, protocols, and payload data. This tool is designed for educational purposes and should be used ethically and legally.

## Features

- Captures network packets on a specified interface.
- Displays source and destination IP addresses.
- Displays protocol information.
- Displays payload data (if available).

## Requirements

- Python 3.x
- Scapy library

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/ZahirSeid/Prodigy_CS_05
    cd Prodigy_CS_05
    ```

2. **Install the required libraries:**

    ```sh
    pip install scapy
    ```

## Usage

1. **Run the tool:**

    ```sh
    python Task-05.py
    ```

2. **Enter the network interface:**

    When prompted, enter the name of the network interface you want to sniff packets on (e.g., `eth0`, `wlan0`).

## Example

```
$ python Task-05.py
Enter the interface to sniff packets (e.g., eth0): eth0
Source IP: 192.168.1.5 | Destination IP: 192.168.1.1 | Protocol: 6
Payload: 485454502f312e3120323030204f4b0d0a446174653a205361742c203233204d617920323032302031393a31303a323820474d540d0a5365727665723a204170616368652f322e342e34352028556e6978204c696e7578207838365f3634292053797374656d2f323032302e392e330d0a5669613a206d61696c746f3a2068656c6c6f4073756e63696c6f2e6e65740d0a436f6e74656e742d547970653a20746578742f68746d6c3b20636861727365743d7574662d380d0a0d0a
```

## Ethical Considerations

This tool should be used responsibly and only on networks where you have permission to monitor traffic. Unauthorized packet sniffing can violate privacy and legal regulations. Ensure that your use of this tool complies with all applicable laws and ethical guidelines.


