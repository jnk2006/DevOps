#!/bin/bash

'''
The log file contains the following fields:

IP address
Date and time
Request method and path
Response status code
Response size
Referrer
User agent

You are required to create a shell script that reads the log file and provides the following information:

Top 5 IP addresses with the most requests
Top 5 most requested paths
Top 5 response status codes
Top 5 user agents
'''

LOG_FILE = /Users/Owner/Documents/DevOps/DevOps/Nginx_Log_Analyser/nginx-access.log

# Check if the log file exists
if [ ! -f "$LOG_FILE" ]; then
    echo "Log file not found: $LOG_FILE"
    exit 1
fi

# Top 5 IP addresses with the most requests
echo "Top 5 IP addresses with the most requests:"
awk '{print $1}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -n 5 | while read count ip; do
    echo "$ip - $count requests"
done

# Top 5 most requested paths
echo -e "\nTop 5 most requested paths:"
awk '{print $7}' Nginx_Log_Analyser/nginx-access.log | sort | uniq -c | sort -nr | head -n 5 | while read count path; do 
    echo "$path - $count requests"
done

# Top 5 response status codes
echo -e "\nTop 5 response status codes:"
awk '{print $9}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -n 5 | while read count code; do
    echo "$code - $count requests"
done

# Top 5 user agents
echo -e "\nTop 5 user agents:"
awk -F'"' '{print $6}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -n 5 | while read count user_agent; do
    echo "$user_agent - $count requests"
done

echo -e "\nAnalysis complete."

# Exit the script
exit 0