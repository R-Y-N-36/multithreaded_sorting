# Concurrent Sorting Algorithms in Python

## Overview

This Python script showcases the concurrent implementation of three popular sorting algorithms – Merge Sort, Bubble Sort, and Quick Sort – using multithreading. The script employs the `threading` module to execute sorting functions concurrently on the same input data array. A locking mechanism is integrated to ensure thread safety during execution.

## Sorting Algorithms

### 1. Merge Sort
- Efficient divide-and-conquer algorithm.
- Splits the array, recursively sorts subarrays, and merges them.

### 2. Bubble Sort
- Simple sorting algorithm with repeated passes.
- Compares adjacent elements and swaps them if they are in the wrong order.

### 3. Quick Sort
- Fast and widely used sorting algorithm.
- Selects a pivot, partitions the array, and recursively sorts the partitions.

## Usage

1. Define the input data in the `data` array.
2. Threads are created for each sorting algorithm using the `Thread` class.
3. Threads are started and joined for synchronized execution.

## Execution

```bash
python Main.py
