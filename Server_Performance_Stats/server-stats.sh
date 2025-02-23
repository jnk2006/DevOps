#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <server-name>"
    exit 1
fi

echo "Fetching stats for $HOST..."
ssh $HOST

###################################
# TOTAL CPU USAGE
###################################
ps -eo pcpu | sort -k 1 -r | awk '{totcpuusage += $1} END {printf "Total CPU usage: %s as of %s", totcpuusage "%", strftime(%a %b %d %T %Z %Y") }'
echo

###################################
# TOTAL MEMORY USAGE
###################################
free -h | grep Mem | awk -F" " 'totmemusage = ($3/$2) * 100 } END {printf "Total Memory usage: %s", totmemusage "%"}'
echo

###################################
# TOTAL DISK USAGE
###################################
echo "Total Disk usage: "
df -h | sort -k 5 -r | awk '{print $1, $6, $5}'
echo

###################################
# TOP 5 PROCESSES BY CPU USAGE
###################################
echo "Top 5 processes by CPU usage: "
ps aux --sort -%cpu | head -n 5 | awk '{printf "%s %s %s ", $3, $1, $2; for (i=11; i<=NF; i++) printf "%s ", $i; print ""}'
echo

###################################
# TOP 5 PROCESSES BY MEMORY USAGE
###################################
echo "Top 5 processes by Memory usage: "
ps aux --sort -%mem | head -n 5 | awk '{printf "%s %s %s ", $4, $1, $2; for (i=11; i<=NF; i++) printf "%s ", $i; print ""}'
echo

###################################
# OS VERSION
###################################
echo "OS Version is $(uname -mrs)"
echo

###################################
# UPTIME
###################################
echo "Uptime: $(uptime)"
echo

###################################
# LOAD AVERAGE
# a metric that shows the number of processes that are waiting in the run-queue (scheduled to run on the CPU) or waiting to be executed, essentially showing how heavily the CPU is being utilized over a specific period of time
###################################
echo "Load Average: ${uptime | grep -oP 'load average: \K.*'}"
echo

###################################
# LOGGED IN USERS
###################################
echo "Logged in users: "
who -u | awk '{print $1}'
echo

###################################
# FAILED LOGINS
###################################
echo "Failed logins: "
grep "Failed" /var/log/auth.log | awk '{print $11}' | uniq -c | sort -nr
echo