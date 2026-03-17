# Port-Scanner

A lightweight multithreaded TCP port scanner written in Python that identifies open ports and their associated services on a target host.

---

## Features

- Multithreaded TCP connection scanning for fast results
- Service detection on open ports
- Configurable timeout and port range
- Input validation for IP address, port range, and timeout

---

## Requirements

- Python 3.x
- No third-party libraries required - used Python standard library only

---

## Usage

Run the scanner with:

```bash
python scanner.py
```

You will be prompted to enter a timeout length, port range, and target IP address.

---

## Example Output

```bash
Starting scan from ports 50 - 500 on host 127.0.0.1
Time length is 1.0 seconds

Port open: 80 | http
Port open: 443 | https
```

---

## Disclaimer

This tool is intended for educational purposes only. Only use it on networks and systems you own or have explicit permission to scan. Unauthorized port scanning may be illegal in your jurisdiction.
