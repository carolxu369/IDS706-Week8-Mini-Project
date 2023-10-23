"""
This module reads data from an input.csv file, processes the data by multiplying 
each value by 2, and writes the processed data to an output.csv file.
"""

import csv
import time
from memory_profiler import profile


def process_data(data):
    """
    Processes the data by multiplying each value by 2.
    """
    return [str(int(x) * 2) for x in data]


@profile
def main():
    """
    Main function that reads data from input.csv, processes it, and writes 
    to output.csv.
    """
    start_time = time.time()

    with open('input.csv', 'r', encoding='utf-8') as infile, \
         open('output.csv', 'w', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            processed_data = process_data(row)
            writer.writerow(processed_data)

    end_time = time.time()
    print(f"Python script executed in {end_time - start_time:.4f} seconds.")


if __name__ == "__main__":
    main()
