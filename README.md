# IDS706-Week8-Mini-Project: Rewrite a Python Script in Rust

This is a Python GitHub Template Repository that includes the following contents:
- A .devcontainer configuration for a Python environment
- A Makefile with commands for setup, testing, and linting
- GitHub Actions for CI/CD
- A requirements.txt for project dependencies
- A Python script
- A Rust script
- Report for comparison in speed and resource usage
  
## Prerequisites

- memory-profiler

## Report

This is the report comparing speed and resource usage for the python and rust.  

Python script executed in 0.0434 seconds.  
Filename: python_script.py  
  
Line #    Mem usage    Increment  Occurrences   Line Contents  
=============================================================  
    18     15.5 MiB     15.5 MiB           1   @profile  
    19                                         def main():  
    20                                             """  
    21                                             Main function that reads data from input.csv, processes it, and writes  
    22                                             to output.csv.  
    23                                             """  
    24     15.5 MiB      0.0 MiB           1       start_time = time.time()  
    25                                               
    26     15.5 MiB      0.0 MiB           2       with open('input.csv', 'r', encoding='utf-8') as infile, \  
    27     15.5 MiB      0.0 MiB           2            open('output.csv', 'w', encoding='utf-8') as outfile:  
    28     15.5 MiB      0.0 MiB           1           reader = csv.reader(infile)  
    29     15.5 MiB      0.0 MiB           1           writer = csv.writer(outfile)  
    30     15.6 MiB      0.0 MiB        1001           for row in reader:  
    31     15.6 MiB      0.0 MiB        1000               processed_data = process_data(row)  
    32     15.6 MiB      0.0 MiB        1000               writer.writerow(processed_data)  
    33                                           
    34     15.6 MiB      0.0 MiB           1       end_time = time.time()  
    35     15.6 MiB      0.0 MiB           1       print(f"Python script executed in {end_time - start_time:.4f} seconds.")  
  

        0.11 real         0.08 user         0.02 sys  
            16384000  maximum resident set size  
                   0  average shared memory size  
                   0  average unshared data size  
                   0  average unshared stack size  
                1675  page reclaims  
                   0  page faults  
                   0  swaps  
                   0  block input operations  
                   0  block output operations  
                   0  messages sent  
                   0  messages received  
                   0  signals received  
                   1  voluntary context switches  
                  21  involuntary context switches  
           974814266  instructions retired  
           288506261  cycles elapsed  
            12354496  peak memory footprint  
  
Finished dev [unoptimized + debuginfo] target(s) in 0.01s  
     Running `target/debug/rust_project`  
Rust script executed in 0.0052 seconds.  
        0.14 real         0.05 user         0.01 sys  
             1687552  maximum resident set size  
                   0  average shared memory size  
                   0  average unshared data size  
                   0  average unshared stack size  
                2298  page reclaims  
                   0  page faults  
                   0  swaps  
                   0  block input operations  
                   0  block output operations  
                   0  messages sent  
                   0  messages received  
                   1  signals received  
                   2  voluntary context switches  
                  71  involuntary context switches  
            50358140  instructions retired  
            16030334  cycles elapsed  
              803264  peak memory footprint  
  
### Some results analysis:  
  
#### Execution Time:
Python:  
Execution Time: 0.0434 seconds  
  
Rust:  
Execution Time: 0.0052 seconds  
  
Analysis:  
The Rust script executed significantly faster than the Python script. The Rust script took approximately 0.0052 seconds while the Python script took 0.0434 seconds. This represents a speed improvement of over 8x when transitioning from Python to Rust for this task.  
  
#### Memory Usage:
Python:  
Peak Memory Footprint: 15.6 MiB  
Maximum Resident Set Size: 16384000 bytes  
  
Rust:  
Peak Memory Footprint: 803264 bytes  
Maximum Resident Set Size: 1687552 bytes  
  
Analysis:  
Rust's memory usage is significantly lower compared to Python. The Python script has a maximum resident set size of 16.3 MB while the Rust script uses only about 1.68 MB. This represents nearly a 10x reduction in memory usage when using Rust over Python for this specific task.  
  
#### Conclusion:
Comparing Python and Rust for this specific task resulted in:  

- A significant improvement in execution speed (over 8x faster with Rust).
- A drastic reduction in memory usage (nearly 10x less with Rust).
- A more efficient execution as evidenced by fewer instructions retired and cycles elapsed with Rust.
  
It's important to note that while Rust offers superior performance in many scenarios, the right tool should be chosen based on the project's specific requirements, as what we discussed in class.