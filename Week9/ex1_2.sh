#!/bin/sh

### Compare two Python scripts and log their execution time

# Get script name
SCRIPT_NAME=$(basename "$0")

# Get user input
echo "Array size: "
read N

echo "Script 1: "
read script1

echo "Script 2: "
read script2

# Define log file
LOGFILE="${script1//.py/}_vs_${script2//.py/}_{$N}.log"

# Append header to the log file
{
    echo "$SCRIPT_NAME"
    echo "-----------------------"
    echo "Array Size: $N"
    echo "Timestamp: $(date)"
    echo ""
} >> "$LOGFILE"

# Run and log Script 1
echo "Running $script1"
{
    echo "Running $script1"
    time python "$script1" "$N"
    echo ""
} &>> "$LOGFILE"

# Run and log Script 2
echo "Running $script2"
{
    echo "Running $script2"
    time python "$script2" "$N"
    echo ""
} &>> "$LOGFILE"

# Run and log base_script.py
echo "Running base_script.py"
{
    echo "Running base_script.py"
    time python base_script.py "$N"
    echo ""
} &>> "$LOGFILE"

# Append footer separator
echo "#########################" >> "$LOGFILE"

echo "Benchmark results saved to $LOGFILE"