#!/bin/bash

# Display all environment variables
echo "Displaying all environment variables:"
env

# Display command-line arguments passed to the script
echo -e "\nDisplaying command-line parameters:"
if [ $# -eq 0 ]; then
    echo "No command-line parameters provided."
else
    for arg in "$@"; do
        echo "$arg"
    done
fi
