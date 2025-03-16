#!/bin/bash

# Command: (base) Mac:~ Owner$ tar -cvf sample_$(date +"%Y%m%d")_$(date +"%H%M%S").tar.gz sample.txt
# log-archive <log-directory>

# Variables
DEST_DIR=/var/log
SOURCE_DIR=$1

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Source directory does not exist"
    exit 1
fi

# Check if the destination directory exists
if [ ! -d "$DEST_DIR" ]; then
    echo "Destination directory does not exist"
    exit 1
fi

# Check if the source directory is empty
if [ ! "$(ls -A $SOURCE_DIR)" ]; then
    echo "Source directory is empty"
    exit 1
fi

# Store the date and time in a variable
DATE=$(date +"%Y%m%d")
TIME=$(date +"%H%M%S")

# Create a tarball of the log files
tar -cvzf $DEST_DIR/log_archive_$DATE_$TIME.tar.gz $SOURCE_DIR/*

# Check if the tarball was created successfully
if [ $? -eq 0 ]; then
    echo "Log files have been archived"
else
    echo "Error archiving log files"
fi
