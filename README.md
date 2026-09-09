# Multi-Client TCP Chat Server & Traffic Simulator

An end-to-end Computer Networks project implementing low-level socket programming, multi-threaded client-server architecture, and network packet analysis.

## Overview
- **TCP Chat Application:** Multi-client concurrent chat system in Python using native `socket` and `threading` libraries with private messaging routing.
- **Traffic Simulation & Packet Crafting:** Network packet crafting and protocol encapsulation (IPv4, TCP, HTTP) using `Scapy` and raw sockets.
- **Analysis:** Captured and analyzed packet flow sessions in Wireshark (`.pcapng`).

## Features
- **Concurrent Connections:** Dedicated listener and sender threads per connected client for non-blocking I/O.
- **Private Messaging:** Dynamic channel routing enabling direct user-to-user chat via `/chat <username>`.
- **Packet Crafting & Inspection:** Data-driven packet crafting from CSV network flows, capturing handshakes and payload transmissions.

## Tech Stack
- Python 3
- Socket & Threading
- Scapy & Pandas
- Wireshark

## Project Files
- `SERVER.PY` — Multi-threaded TCP chat server
- `CLIENT.PY` — Terminal-based chat client
- `traffic_simulator.ipynb` — Packet crafting and simulation notebook
- `group03_http_input.csv` — Network traffic scenario input
- `*.pcapng` — Wireshark network capture traces
