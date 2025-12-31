#!/bin/bash

# ===============================
# Network Scanner Script
# ===============================

# ask user for target
echo "Enter target (IP or domain):"
read target

# result file
result_file="$HOME/scan-complet.txt"

# start scan
echo "Starting Network Scan..." > $result_file
echo "Target: $target" >> $result_file
echo "============================" >> $result_file

# -------------------------------
# ping test (10 times)
# -------------------------------
echo "" >> $result_file
echo "PING TEST (10 packets)" >> $result_file
echo "----------------------------" >> $result_file
ping -c 10 $target >> $result_file

# -------------------------------
# nslookup
# -------------------------------
echo "" >> $result_file
echo "NSLOOKUP RESULT" >> $result_file
echo "----------------------------" >> $result_file
nslookup $target >> $result_file

# -------------------------------
# traceroute
# -------------------------------
echo "" >> $result_file
echo "TRACEROUTE RESULT" >> $result_file
echo "----------------------------" >> $result_file
traceroute $target >> $result_file

# -------------------------------
# curl
# -------------------------------
echo "" >> $result_file
echo "CURL RESULT" >> $result_file
echo "----------------------------" >> $result_file
curl -I $target >> $result_file

# -------------------------------
# nmap
# -------------------------------
echo "" >> $result_file
echo "NMAP SCAN RESULT" >> $result_file
echo "----------------------------" >> $result_file
nmap $target >> $result_file

# finish
echo "" >> $result_file
echo "Scan completed successfully" >> $result_file

echo "Scan completed"
echo "Results saved in $result_file"

