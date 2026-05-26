# Mini Database Engine with Multiple Data Structures

A Python-based Mini Database Engine developed for the **Data Structures & Algorithms** course.

This project simulates core database functionalities using fundamental data structures and algorithms such as:
- Lists
- Hash Tables
- Searching Algorithms
- Sorting Algorithms
- Query Processing
- Performance Benchmarking

---

# Features

## CRUD Operations

- Insert new records
- Display records
- Update records
- Delete records

---

## Searching Algorithms

### Sequential Search
- Traverses records one by one
- Time Complexity: `O(n)`

### Hash Search
- Uses Hash Table indexing
- Average Time Complexity: `O(1)`

---

## Sorting Algorithms

### Quick Sort
- Divide and Conquer algorithm
- Fast average performance

### Merge Sort
- Stable sorting algorithm
- Predictable performance

Supported sorting:
- Title
- Release Year
- Country

Order options:
- Ascending
- Descending

---

## Query Engine

Supports simple database-like filtering:
- Equal (`=`)
- Greater than (`>`)
- Less than (`<`)

Example:
```python
release_year > 2018
country = "Japan"
```

---

## Benchmarking

Compare performance between:
- Sequential Search
- Hash Search

Uses:
```python
time.perf_counter()
```

to measure execution time.

---

# Technologies Used

- Python
- Pandas
- Tabulate

---

# Project Structure

```text
mini-database-engine/
│
├── main.py
│
├── data/
│   └── data.csv
│
├── structures/
│   ├── table.py
│   └── hash_index.py
│
├── algorithm/
│   └── sorting.py
│
├── query/
│   └── query_engine.py
│
├── benchmark/
│   └── benchmark.py
│
└── README.md
```

---

# Data Structures Used

| Data Structure | Purpose |
|---|---|
| List | Main record storage |
| Dictionary / Hash Table | Fast indexing |
| Recursion | Sorting algorithms |

---

# Algorithms Used

| Algorithm | Complexity |
|---|---|
| Sequential Search | O(n) |
| Hash Search | O(1) average |
| Quick Sort | O(n log n) average |
| Merge Sort | O(n log n) |

---

# How to Run

## 1. Install Required Libraries

```bash
pip install pandas tabulate
```

---

## 2. Run the Program

```bash
python main.py
```

---

# Example Menu

```text
========== MINI DATABASE ENGINE ==========

1. Display Records
2. Insert Record
3. Search Record (Sequential)
4. Update Record
5. Delete Record
6. Count Records
7. Hash Search
8. Benchmark Search
9. Sort Records
10. Query Engine
11. Exit
```

---

# Example Benchmark Result

```text
===== BENCHMARK RESULTS =====

Sequential Search Time: 0.004231 seconds
Hash Search Time: 0.000002 seconds
```

---

# Learning Outcomes

This project helped reinforce understanding of:
- Data Structures
- Algorithm Complexity
- Performance Optimization
- Recursive Algorithms
- Modular System Design

---

# Future Improvements

Possible future extensions:
- Graphical User Interface (GUI)
- Persistent Storage
- SQL-like Parser
- AVL / B+ Tree Indexing
- Multi-condition Queries

---

# About me

Hi! My name is Bui Dinh Tuyen. I'm a student with a strong interest in **Data Analytics, Data Science, and Data Engineering**.  
I enjoy working with data to design efficient data models, build data pipelines, and generate insights through analytical queries.
