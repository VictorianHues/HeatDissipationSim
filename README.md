# OpenMP Assignment

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Compilation](#compilation)
5. [Usage](#usage)
6. [Address Tracing Scripts](#address-tracing-scripts)
7. [Program Command Line Arguments](#program-command-line-arguments)
8. [File Structure](#file-structure)
9. [References](#references)
10. [License](#license)

## Introduction

This project demonstrates parallel programming concepts using OpenMP. The implementation focuses on optimizing performance by leveraging shared-memory multiprocessing.

## Prerequisites

Ensure you have the following installed on your system:

- A C/C++ compiler with OpenMP support (e.g., GCC, Clang, or MSVC)
- A Unix-based environment (Linux/macOS) or Windows with MinGW or WSL
- Make (optional, for build automation)

## Installation

1. Clone the repository (if applicable):

   ```sh
   git clone https://github.com/VictorianHues/HeatDissipationSim.git
   ```

2. Ensure OpenMP support is available by running:

   ```sh
   gcc -fopenmp --version  # For GCC
   clang -fopenmp --version  # For Clang
   ```

3. If missing, install GCC with OpenMP support:

   - **Ubuntu/Debian:** `sudo apt install gcc libgomp1`
   - **MacOS (with Homebrew):** `brew install llvm`
   - **Windows (MinGW-w64):** Ensure you have `libgomp` installed

4. To generate address traces from the heat dissipation implementation, untar the Intel Pin software and Address trace library into a directory outside of the project repo (I use `\home\user-name\projects\`):

   ``` sh
   tar xf pin-3.27-98718-gbeaa5d51e-gcc-linux.tar.gz
   tar xf mcps-tracer.tar.gz
   ```

5. Add a symbolic link to refer to the Pin install:

   ``` sh
   ln -s pin-3.27-98718-gbeaa5d51e-gcc-linux/pin
   ```

6. Install the tracing software:

   ``` sh
   export PATH+=:/path/to/pintool/pin
   export PIN_ROOT=/path/to/pintool/pin
   cd mcps-tracer
   make
   ```

7. Return to the project repository and enter both the `heat_seq` and `heat_omp` directories to configure the make files, setting:

   ``` sh
   MCPS_TRACER_ROOT=/path/to/mcps-tracer
   ```

## Compilation
Compile either the `heat_seq` or `heat_omp` implementations and generate executeable:

   ``` sh
   make
   # or
   make all
   ```

## Usage

Run either the `heat_seq` or `heat_omp` implementations using the following options:

- Runs the program with pre-defined arguments `-n 150 -m 100 -i 42 -k 1000 -e 0.1 -c ../images/pat1_100x150.pgm -t ../images/pat1_100x150.pgm -L -100.0 -H 100.0 -p 1 -r 0`.

   ``` sh
   make run # heat_omp takes P integer argument for processor number
   ```

- Runs the program with custom arguments passed via the `ARGS` variable.

   ``` sh
   make run_args ARGS="... -i 10 -p 4 ..."
   ```

- Runs the program with tracing enabled using Intel's `pin` tool and MCPS tracer with pre-defined arguments `-n 150 -m 100 -i 42 -k 1000 -e 0.1 -c ../images/pat1_100x150.pgm -t ../images/pat1_100x150.pgm -L -100.0 -H 100.0 -p 1 -r 0`.

   ``` sh
   make run_with_tracing  # heat_omp takes P integer argument for processor number
   ```

- Similar to `run_with_tracing`, but allows passing additional arguments via the `ARGS` variable.

   ``` sh
   make run_with_tracing_args ARGS="... -i 10 -p 4 ..."
   ```

- Remove all generated files, executeable, and address logs.

   ``` sh
   make clean
   ```

## Address Tracing Scripts

Convert addresse logs generated when using `run_with_tracing` into a memory trace file using a Python script.

   ``` sh
   make traces
   ```

Use Python to print the trace file

   ``` sh
   python3 ../ scripts/trace_printer.py memory_trace.trf
   ```

## Program Command Line Arguments

| Parameter        | Definition / Purpose |
|-----------------|-----------------------------|
| `-n` / `-N` (Cylinder Height)  | Defines the number of rows in the simulation grid. |
| `-m` / `-M` (Cylinder Width)  | Specifies the number of columns in the simulation grid. |
| `-i` (Max Iterations)  | Sets the maximum number of iterations before termination. |
| `-k` (Reduction Period)  | Determines the number of iterations between reduction operations. |
| `-e` (Convergence Threshold)  | Specifies the threshold value for convergence detection. |
| `-c` (Conductivity File)  | Path to the PGM file containing the material conductivity values. |
| `-t` (Initial Temperature File)  | Path to the PGM file containing the initial temperature distribution. |
| `-L` (Coldest Temperature)  | The minimum temperature value for input/output images. |
| `-H` (Warmest Temperature)  | The maximum temperature value for input/output images. |
| `-p` (Number of Threads)  | Defines the number of OpenMP threads to be used for parallel execution. |
| `-r` (Print Reports)  | Enables periodic reporting of simulation progress during execution. |

## File Structure

Below is the expected directory structure for the project:

```sh
├── heat_omp/          # OpenMP Heat Dissipation Source Code
├── heat_seq/          # Sequential Heat Dissipation Source Code
├── src/               # Template source code
├── include/           # Header files
├── scripts/           # Python scripts for address traces
├── images/            # Temperature and Conductivity Grids
├── trace_files/       # Trace file compiler and complete traces
├── Makefile           # Build tarball
├── reference_output/  # Temperature Grid Reference output
├── README.md          # Project documentation
├── mcps-tracer.tar.gz # Address Trace Library
└── pin-3.27-98718-gbeaa5d51e-gcc-linux.tar.gz
   # Intel Pin software
```

## References

- [OpenMP Official Documentation](https://www.openmp.org/)
- [GCC OpenMP Guide](https://gcc.gnu.org/onlinedocs/libgomp/)
- [AddressSanitizer Documentation](https://clang.llvm.org/docs/AddressSanitizer.html)
- [Valgrind Documentation](http://valgrind.org/)

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Let me know if you need any modifications!
