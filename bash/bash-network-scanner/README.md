# Network Scanner (Bash)

## Description
This project is a simple Bash script that performs a basic network scan
using common Linux networking tools.

The script allows the user to enter either an IP address or a domain name
and then runs several network checks sequentially.
All results are saved into a single text file.

The project focuses on clarity, order, and understanding how Linux
networking tools work together.

---

## Script Overview

The script performs the following steps:

1. Ask the user to enter a target (IP address or domain name)
2. Create a result file in the user's home directory
3. Run multiple network tools in sequence
4. Save all outputs into one text file

---

## Tools Used

The script uses the following tools:

- `ping` (10 packets)
- `nslookup`
- `traceroute`
- `curl`
- `nmap`

Each tool’s output is clearly separated inside the result file.

---

## Output File

All scan results are saved to:
