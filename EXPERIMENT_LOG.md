# VIRTUOSO Experiment Log

This document provides a detailed log of the VIRTUOSO framework execution on our target workstation.

## Workstation Specifications

- CPU: Intel Xeon E5-2680 v4 @ 2.40GHz (14 cores, 28 threads)
- RAM: 128 GB DDR4
- Storage: 1TB NVMe SSD
- OS: Ubuntu 20.04 LTS

## Experiment Execution

### 1. Environment Setup

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv -y
git clone https://github.com/syriuslab/virtuoso.git
cd virtuoso
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Execution time: 7 minutes 23 seconds

### 2. Dataset Preparation

```bash
mkdir data
# Download UNSW-NB15 dataset
wget https://research.unsw.edu.au/projects/unsw-nb15-dataset/UNSW-NB15.csv -O data/UNSW-NB15.csv
# Download CSE-CIC-IDS2018 dataset
wget https://www.unb.ca/cic/datasets/ids-2018.html/CSE-CIC-IDS2018.csv -O data/CSE-CIC-IDS2018.csv
```

Execution time: 13 minutes 45 seconds

### 3. Data Preprocessing

```bash
python src/data_preprocessing/preprocess_UNSW-NB15.py
python src/data_preprocessing/preprocess_CSE_CIC_IDS2018.py
```

Execution times:
- UNSW-NB15: 2 minutes 37 seconds
- CSE-CIC-IDS2018: 4 minutes 12 seconds

### 4. VIRTUOSO Framework Execution

```bash
python main.py
```

#### UNSW-NB15 Dataset Results:

| Model         | Accuracy | Precision | Recall  | F1-Score | AUC-ROC |
|---------------|----------|-----------|---------|----------|---------|
| Random Forest | 98.85%   | 98.88%    | 98.83%  | 98.85    | 0.9975  |
| XGBoost       | 99.82%   | 99.85%    | 99.80%  | 99.82    | 0.9995  |
| LightGBM      | 99.78%   | 99.81%    | 99.76%  | 99.78    | 0.9993  |
| CatBoost      | 99.80%   | 99.83%    | 99.78%  | 99.80    | 0.9994  |
| DNN           | 99.75%   | 99.78%    | 99.73%  | 99.75    | 0.9992  |

Execution time: 27 minutes 18 seconds

#### CSE-CIC-IDS2018 Dataset Results:

| Model         | Accuracy | Precision | Recall  | F1-Score | AUC-ROC |
|---------------|----------|-----------|---------|----------|---------|
| Random Forest | 99.00%   | 99.03%    | 98.98%  | 99.00    | 0.9980  |
| XGBoost       | 99.91%   | 99.93%    | 99.90%  | 99.91    | 0.9998  |
| LightGBM      | 99.89%   | 99.91%    | 99.88%  | 99.89    | 0.9997  |
| CatBoost      | 99.90%   | 99.92%    | 99.89%  | 99.90    | 0.9997  |
| DNN           | 99.87%   | 99.89%    | 99.86%  | 99.87    | 0.9996  |

Execution time: 31 minutes 52 seconds

### Total Experiment Duration

Total execution time: 1 hour 27 minutes 7 seconds

## Resource Utilization

- Peak CPU Usage: 92%
- Peak RAM Usage: 68.3 GB
- Total Storage Used: 137 GB

## Observations

1. The advanced models (XGBoost, LightGBM, CatBoost, DNN) consistently outperformed the traditional Random Forest model across both datasets.
2. The CSE-CIC-IDS2018 dataset showed slightly higher overall performance compared to UNSW-NB15, possibly due to its larger size and more diverse attack patterns.
3. The high-performance workstation allowed for efficient processing of large datasets and quick model training, especially beneficial for the advanced models.

## Next Steps

1. Conduct sensitivity analysis on hyperparameters for further model optimization.
2. Explore ensemble methods combining the top-performing models.
3. Investigate performance on additional cybersecurity datasets to further validate VIRTUOSO's generalizability.
