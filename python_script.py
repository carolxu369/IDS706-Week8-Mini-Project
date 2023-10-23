import csv
import time
from memory_profiler import profile

def process_data(data):

    return [str(int(x) * 2) for x in data]

@profile
def main():
    start_time = time.time()

    with open('input.csv', 'r') as infile, open('output.csv', 'w') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            processed_data = process_data(row)
            writer.writerow(processed_data)

    end_time = time.time()
    print(f"Python script executed in {end_time - start_time:.4f} seconds.")

if __name__ == "__main__":
    main()