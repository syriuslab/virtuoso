# REPLICATION\_GUIDE.md

## Objective

This guide explains how to replicate the full set of experiments described in the VIRTUOSO paper, using public datasets and standard cloud environments. It covers preprocessing, model training, and evaluation pipelines.

## Requirements

* Python 3.8+
* Google Colab (free tier) or equivalent cloud VM
* Dependencies listed in `requirements.txt` (e.g., scikit-learn, XGBoost, LightGBM, CatBoost, TensorFlow)
* Datasets:

  * UNSW-NB15 CSV: [https://research.unsw.edu.au/projects/unsw-nb15-dataset](https://research.unsw.edu.au/projects/unsw-nb15-dataset)
  * CSE-CIC-IDS2018 Web Subset: pre-filtered subset (available in Colab environment)

## Folder Structure

```
virtuoso/
├── data/
│   ├── UNSW_X.csv
│   ├── UNSW_y.csv
│   ├── IDS_X_web.csv
│   └── IDS_y_web.csv
├── scripts/
│   ├── run_xgboost.py
│   ├── run_lightgbm.py
│   ├── run_catboost.py
│   └── run_dnn.py
├── utils/
│   └── metrics_plotting.py
├── requirements.txt
├── config.yaml
```

## Steps to Reproduce

### 1. Prepare Environment

Use `pip install -r requirements.txt` to install all Python dependencies.

### 2. Preprocess Data

The preprocessing is handled directly inside each script, including:

* Label encoding of categorical features
* StandardScaler normalization (for DNN)
* Stratified 5-fold split
* SMOTE applied to training folds only

### 3. Train Models

Each script handles one model:

* `run_xgboost.py`: runs XGBoost with fixed hyperparameters
* `run_lightgbm.py`: uses LGBMClassifier with stratified CV
* `run_catboost.py`: uses CPU-based CatBoost with SMOTE
* `run_dnn.py`: runs TensorFlow-based DNN with early stopping and ReduceLR

Each script outputs averaged metrics and generates:

* ROC Curve (saved as PNG)
* Precision-Recall Curve
* AUC/PR scores

### 4. Evaluate Results

All scripts produce the following metrics (averaged across folds):

* Accuracy
* Precision
* Recall
* F1 Score
* MCC
* AUC-ROC
* AUC-PR


## Notes

* Results are deterministic thanks to fixed random seed (42).
* All scripts are runnable on Google Colab in < 30 minutes each.
* You may replace datasets with newer ones to extend the analysis.
