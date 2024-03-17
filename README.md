# Custom Packet Sniffing Tool

This is a custom packet sniffing tool written in Python using libraries such as `socket`, `struct`, `textwrap`, and `scapy`. The tool allows for tight and loose sniffing of network packets and can extract information such as Ethernet frames and HTTP requests.

## Prerequisites
Make sure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

## Installation
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Navigate to the project directory:
   ```
   cd your-repo-name
   ```

3. Install the required libraries using pip:
   ```
   pip install -r requirements.txt
   ```

## Requirements
The `requirements.txt` file contains the necessary module for this project:
```
scapy
```

## Usage
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the script using Python:
   ```
   python sniffer.py
   ```

## Features
- Tight and loose packet sniffing options.
- Extraction of Ethernet frame information.
- Detection of HTTP requests.

## Example
Here's an example of how to use the tool:

1. Choose the sniffing mode (tight or loose).
2. If you choose tight sniffing, enter the interface for scanning.
3. View the sniffed packets and extracted information.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.
