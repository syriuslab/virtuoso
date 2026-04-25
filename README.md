# VIRTUOSO Pipeline

**VIRTUOSO** stands for **VIRTual Unified Operation Security Optimiser**.  
This repository contains an end to end research pipeline for multi layer cyber security evaluation across three complementary security views:

- **Channel 1**: network intrusion detection on benchmark IDS datasets
- **Channel 2**: behavioural anomaly detection on AWS CloudTrail logs
- **Channel 3**: CNAPP style static security inspection from infrastructure scan reports

The pipeline combines classical machine learning, deep learning, adversarial robustness analysis, statistical testing, computational cost profiling, and paper ready export utilities in a single notebook oriented workflow.

---

## What this pipeline does

The notebook implements a unified experimental workflow that:

1. **Prepares benchmark datasets** for supervised intrusion detection.
2. **Trains and evaluates Tier 1 tabular models** including Random Forest, XGBoost, LightGBM, and CatBoost.
3. **Trains a DNN baseline** with repeated stratified splits.
4. **Assesses robustness under adversarial perturbations** using FGSM and PGD.
5. **Builds a behavioural anomaly detector for CloudTrail** with an Autoencoder and Isolation Forest.
6. **Parses CNAPP findings** from Checkov and Trivy reports.
7. **Aggregates risk signals across layers** into a consolidated risk snapshot.
8. **Exports paper ready tables, figures, and CSV artefacts** for downstream reporting.

This design is useful when the goal is not only high predictive performance, but also a broader security posture assessment that spans runtime traffic, cloud audit behaviour, and infrastructure misconfiguration signals.

---

## Main components

### 1. Channel 1: Intrusion Detection
The supervised IDS layer uses two public datasets:

- **UNSW-NB15**
- **CSE-CIC-IDS2018 WEB subset** using the Thursday-22 and Friday-23 attack traffic files

The pipeline performs dataset specific preprocessing, then evaluates:

- Random Forest
- XGBoost
- LightGBM
- CatBoost
- DNN baseline

The evaluation includes:

- 5 fold stratified cross validation for Tier 1 models
- repeated train test splits for DNN
- per fold tracking of metrics
- train and inference timing
- train test gap inspection for overfitting analysis
- hyperparameter sensitivity analysis
- paper ready summary tables and bar charts

### 2. Channel 2: CloudTrail Behavioural Anomaly Detection
The cloud audit layer loads **flAWS CloudTrail logs** and converts raw events into session level features. It then trains:

- a dense **Autoencoder** for reconstruction based anomaly detection
- an **Isolation Forest** for unsupervised anomaly detection

This layer also includes a stress test based on adversarial style perturbations of the Autoencoder input representation.

### 3. Channel 3: CNAPP Layer
The CNAPP layer ingests infrastructure security findings from:

- **Checkov** JSON reports
- **Trivy** JSON reports

If these reports are absent, the notebook can fall back to synthetic examples so that the downstream risk aggregation stages remain executable.

### 4. Risk Engine
The final risk layer merges outputs from all channels into a compact risk snapshot. In practice, this enables a single analytical view over:

- IDS robustness degradation under adversarial perturbation
- CloudTrail anomaly sensitivity
- CNAPP finding volume and severity

---

## Notebook structure

The notebook is organised as follows:

- **Environment setup** with portable paths and partial auto download support
- **Shared utilities** for metrics and timing
- **UNSW-NB15 preprocessing**
- **CSE-CIC-IDS2018 WEB preprocessing**
- **DNN definition and repeated training**
- **Tier 1 model training with per fold tracking**
- **Statistical significance testing** with Friedman and Nemenyi procedures
- **Paper ready tables and figures**
- **Hyperparameter sensitivity and cost analysis**
- **Dataset description and class breakdown**
- **Adversarial evaluation** using FGSM and PGD
- **CloudTrail loading and anomaly detection**
- **CloudTrail stress testing**
- **CNAPP parsing**
- **Risk aggregation**
- **Artefact export and global summary**

---

## Datasets

### UNSW-NB15
Used for supervised binary intrusion detection. The notebook expects:

- `UNSW_NB15_training-set.csv`
- `UNSW_NB15_testing-set.csv`

The pipeline attempts automatic download through `kagglehub`. If that fails, the files should be placed manually in `data/`.

### CSE-CIC-IDS2018
Only the web attack subset is used. The notebook expects:

- `Thursday-22-02-2018_TrafficForML_CICFlowMeter.csv`
- `Friday-23-02-2018_TrafficForML_CICFlowMeter.csv`

The download is attempted from the public S3 bucket via AWS CLI with `--no-sign-request`.

### CloudTrail flAWS logs
The notebook downloads and extracts the public `flaws_cloudtrail_logs.tar` archive if it is not already present.

---

## Requirements

The notebook relies mainly on the following Python packages:

- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`
- `tensorflow`
- `xgboost`
- `lightgbm`
- `catboost`
- `scikit-posthocs`
- `awscli` for public S3 download support
- `kagglehub` for UNSW dataset retrieval

A notebook environment such as **Google Colab** is supported, but the pipeline also runs in a local Python environment with a valid working directory.

### Citation

If you use this work, please cite:

```bibtex
@article{anwar2026virtuoso,
  title   = {VIRTUOSO: A Multilayer Cloud Security and Risk Management Framework},
  author  = {Anwar, Raja Waseem and Pastore, Flavio and Abdullah, Tariq},
  journal = {Computers},
  volume  = {15},
  number  = {5},
  pages   = {272},
  year    = {2026},
  doi     = {10.3390/computers15050272},
  url     = {https://www.mdpi.com/2073-431X/15/5/272}
}
```

---

