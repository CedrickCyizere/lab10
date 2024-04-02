#!/usr/bin/env python3

import re
import sys
import subprocess

def main():
    if len(sys.argv) < 3:
        sys.exit(0)
    date_from = sys.argv[1]
    date_to   = sys.argv[2] 

    # Get the list of installed packages with their installation dates
    result = subprocess.run(['grep', ' install ', '/Users/cedrick/Downloads/lab10/10/B/dpkg.log'], stdout=subprocess.PIPE)
    lines = result.stdout.decode('utf-8').split('\n')

    # Iterate over each line
    for line in lines:
        # Split the line into words
        words = line.split()

        # Check if the line has the correct number of words and the date is within the range
        if len(words) >= 3 and date_from <= words[0] <= date_to:
            # Get the package name without the architecture
            package_name = re.sub(r':amd64', '', words[3])

            # Print the date and package name
            print(f"{words[0]}: {package_name}")

if __name__ == "__main__":
    main()

