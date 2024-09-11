# SFPsimulations
Monte Carlo simulations for the Drosophila seminal fluid proteome and gene age analysis. This project performs resampling-based simulations to assess the association between subnetworks and gene ages using observed data and 100,000 simulated datasets.

## Overview
The analysis consists of two rounds of simulations:

- **Round 1**: Resampling gene ages across 6 subnetworks (n1-n6)
- **Round 2**: Resampling gene ages across 3 subnetworks (n1-n3)

For each round, the scripts resample gene ages (A-E) without replacement, evaluate conditions based on the resampled and observed data, and summarize the results.

---

### Round 1: 6 Subnetworks, 100,000 Resamplings
- **Script**: `monte_carlo_1.py`
- **Input File**: `Table1_1.csv` (contains gene age data for 6 subnetworks)
    - Column C: Gene ages (A-E)
    - Subnetworks: n1 to n6
- **Output Files**:
    - `Table2_1.txt`: Contains resampled tables for each of the 100,000 iterations.
    - `resampling_results_1.txt`: Summarizes results based on 11 relevant IF conditions, indicating whether the resampled values in `Table2_1.txt` are equal to or larger than the observed values.

---

### Round 2: 3 Subnetworks, 100,000 Resamplings
- **Script**: `monte_carlo_2.py`
- **Input File**: `Table1_2.csv` (contains gene age data for 3 subnetworks)
    - Column C: Gene ages (A-E)
    - Subnetworks: n1 to n3
- **Output Files**:
    - `Table2_2.txt`: Contains resampled tables for each of the 100,000 iterations.
    - `resampling_results_2.txt`: Summarizes results based on 11 relevant IF conditions, indicating whether the resampled values in `Table2_2.txt` are equal to or larger than the observed values.

---

### What are the IF Conditions?
The IF conditions evaluate the resampled data by comparing each resampled value to the corresponding observed value in `Table 2`. For each comparison:
- **1** indicates the resampled value is equal to or greater than the observed value.
- **0** indicates the resampled value is less than the observed value.

The summary file (`resampling_results.txt`) records these results for further analysis.

---

### Usage
1. Clone the repository and ensure you have the required dependencies (e.g., `pandas`).
2. To run the simulation for Round 1:
    ```bash
    python monte_carlo_1.py
    ```
3. To run the simulation for Round 2:
    ```bash
    python monte_carlo_2.py
    ```

Make sure the corresponding input files (`Table1_1.csv` or `Table1_2.csv`) are in the correct directory before running the scripts.
