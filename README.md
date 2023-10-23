# IDS706-Week8-Mini-Project

Finished dev [unoptimized + debuginfo] target(s) in 0.04s
     Running `target/debug/rust_project`
Rust script executed in 0.0089 seconds.
        0.35 real         0.05 user         0.02 sys
             1818624  maximum resident set size
                   0  average shared memory size
                   0  average unshared data size
                   0  average unshared stack size
                1551  page reclaims
                 759  page faults
                   0  swaps
                   0  block input operations
                   0  block output operations
                   0  messages sent
                   0  messages received
                   1  signals received
                  91  voluntary context switches
                 274  involuntary context switches
            54840740  instructions retired
            22658834  cycles elapsed
              950784  peak memory footprint

Python script executed in 0.0436 seconds.
Filename: python_script.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     9     15.4 MiB     15.4 MiB           1   @profile
    10                                         def main():
    11     15.4 MiB      0.0 MiB           1       start_time = time.time()
    12                                         
    13     15.4 MiB      0.0 MiB           1       with open('input.csv', 'r') as infile, open('output.csv', 'w') as outfile:
    14     15.4 MiB      0.0 MiB           1           reader = csv.reader(infile)
    15     15.4 MiB      0.0 MiB           1           writer = csv.writer(outfile)
    16                                                 
    17     15.5 MiB      0.0 MiB        1001           for row in reader:
    18     15.5 MiB      0.0 MiB        1000               processed_data = process_data(row)
    19     15.5 MiB      0.0 MiB        1000               writer.writerow(processed_data)
    20                                         
    21     15.5 MiB      0.0 MiB           1       end_time = time.time()
    22     15.5 MiB      0.0 MiB           1       print(f"Python script executed in {end_time - start_time:.4f} seconds.")


        0.14 real         0.08 user         0.03 sys
            16285696  maximum resident set size
                   0  average shared memory size
                   0  average unshared data size
                   0  average unshared stack size
                1648  page reclaims
                  24  page faults
                   0  swaps
                   0  block input operations
                   0  block output operations
                   0  messages sent
                   0  messages received
                   0  signals received
                 223  voluntary context switches
                  32  involuntary context switches
           990878828  instructions retired
           304546759  cycles elapsed
            12206848  peak memory footprint