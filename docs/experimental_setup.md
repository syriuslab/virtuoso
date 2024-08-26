# Experimental Setup for VIRTUOSO

---

## Table of Contents
- [Hardware Specifications](#hardware-specifications)
- [Software and Tools](#software-and-tools)
- [Datasets](#datasets)
- [Experimental Process](#experimental-process)
- [Reproducibility](#reproducibility)

---

## Hardware Specifications

All experiments were conducted on a high-performance workstation with the following specifications:

| Component | Specification |
|-----------|---------------|
| CPU       | Intel Xeon E5-2680 v4 @ 2.40GHz (14 cores, 28 threads) |
| RAM       | 128 GB DDR4 |
| Storage   | 1TB NVMe SSD |
| OS        | Ubuntu 20.04 LTS |

---

## Software and Tools

The following software and tools were used in our experiments:

### Core Software
- **Weka 3.8.5**: Used for traditional machine learning models
- **Python 3.8.5**: Used for advanced models and data preprocessing

### Key Python Libraries
```
scikit-learn == 0.24.2
XGBoost      == 1.4.2
LightGBM     == 3.2.1
TensorFlow   == 2.4.0
pandas       == 1.2.4
numpy        == 1.19.5
```

---

## Datasets

Two primary datasets were used in this study:

1. **UNSW-NB15 dataset**: For network intrusion detection
   - Source: [UNSW-NB15 Dataset](https://research.unsw.edu.au/projects/unsw-nb15-dataset)
   - Used subset: Approximately 1 million flow records

2. **CSE-CIC-IDS2018 dataset**: For web attack analysis
   - Source: [CSE-CIC-IDS2018 Dataset](https://www.unb.ca/cic/datasets/ids-2018.html)
   - Used subset: Approximately 2 million web log entries

---

## Experimental Process

Our experimental process consisted of the following key steps:

### 1. Data Preparation
- Preprocessing of datasets using Python scripts
  > See `src/data_preprocessing/` for detailed scripts
- Feature selection and normalization
- Conversion to formats compatible with both Weka (.arff) and Python (.csv)

### 2. Model Training and Evaluation
#### Weka
- Used for training and evaluating traditional models:
  * Random Forest
  * SVM
  * Naive Bayes
  * J48
- Configuration files available in `src/weka_configs/`

#### Python
- Used for advanced models:
  * XGBoost
  * LightGBM
  * CatBoost
  * Deep Neural Networks (DNN)
  * Long Short-Term Memory (LSTM)
- Implementation in `src/intelligent_security_layer/`

> All models were evaluated using 10-fold cross-validation

### 3. Performance Metrics
The following metrics were calculated for all models:
- Accuracy
- Precision
- Recall
- F1-score
- AUC-ROC

### 4. Results Integration and Analysis
- Results from both Weka and Python collected and compared
- Graphs and tables generated using Python scripts

---

## Reproducibility

To reproduce the experimental results:

1. Set up the environment as described in this document
2. Follow the instructions in the main `README.md` file
3. Use the provided scripts in `src/data_preprocessing/` for data preparation
4. Execute Weka configurations and Python scripts as described in their respective directories
5. Refer to individual script documentation for detailed usage instructions

> For any questions or issues regarding the experimental setup, please open an issue in the GitHub repository.


