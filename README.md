
# Multithreaded Sorting Algorithms

This repository implements three popular sorting algorithms (Merge Sort, Quick Sort, and Bubble Sort) using multithreading in Python. Each algorithm runs in its own thread, demonstrating basic concurrency and synchronization using locks.

## Table of Contents
- [Algorithms](#algorithms)
- [Usage](#usage)
- [Requirements](#requirements)
- [License](#license)

## Algorithms
1. **Merge Sort**: A divide-and-conquer algorithm that sorts by recursively dividing the array into halves, sorting each half, and then merging the sorted halves.
2. **Quick Sort**: Another divide-and-conquer algorithm that selects a 'pivot' element and partitions the array into elements less than and greater than the pivot, recursively sorting the partitions.
3. **Bubble Sort**: A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Multithreaded-Sorting-Algorithms.git
   cd Multithreaded-Sorting-Algorithms
   ```

2. Run the `main.py` file to execute all sorting algorithms in parallel:
   ```bash
   python main.py
   ```

## Requirements
- Python 3.x

No additional packages are required for this repository since it uses only the built-in Python libraries (`threading` and `time`).