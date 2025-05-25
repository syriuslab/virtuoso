
## Overview

This document provides a detailed log of the experiments conducted using the VIRTUOSO framework, following the methodology described in the accompanying paper. Two datasets were used: **UNSW-NB15** and **CSE-CIC-IDS2018-WEB**, each evaluated across multiple machine learning algorithms.

---

## Datasets

* **UNSW-NB15**: A real-world network traffic dataset that includes a variety of attack types and normal traffic.
* **CSE-CIC-IDS2018-WEB**: A curated subset focusing on web-based attacks from the simulated CSE-CIC-IDS2018 dataset.

---

## Models Evaluated

* Random Forest
* XGBoost
* LightGBM
* CatBoost
* Deep Neural Network (DNN)

---

## Metrics Used

Each model was evaluated using the following performance metrics:

1. **Accuracy**
2. **Precision**
3. **Recall**
4. **F1 Score**
5. **AUC-ROC**
6. **False Positive Rate (FPR)**
7. **False Negative Rate (FNR)**
8. **Matthews Correlation Coefficient (MCC)**

These metrics were computed as per Equations (1) to (8) in the manuscript.

---

## Results Summary

### UNSW-NB15

* **XGBoost**: Accuracy = 99.68%, AUC-ROC = 0.9998
* **Random Forest**: Accuracy = 99.65%, AUC-ROC = 0.9997
* **LightGBM**: Accuracy = 99.57%, AUC-ROC = 0.9999
* **CatBoost**: Accuracy = 99.55%, AUC-ROC = 0.9997
* **DNN**: Accuracy = 97.49%, AUC-ROC = 0.9281

### CSE-CIC-IDS2018-WEB

* **LightGBM**: Accuracy = 99.35%, AUC-ROC = 0.9986
* **XGBoost**: Accuracy = 99.19%, AUC-ROC = 0.9988
* **CatBoost**: Accuracy = 99.19%, AUC-ROC = 0.9985
* **Random Forest**: Accuracy = 99.19%, AUC-ROC = 0.9971
* **DNN**: Accuracy = 98.28%, AUC-ROC = 0.9971

---

## Hardware & Execution

All models were trained and validated using Google Colab with the following resources:

* **GPU**: Tesla T4 (free tier)
* **RAM**: 12 GB
* **CPU**: 2-core Xeon

Total runtime for each complete pipeline (per model): **< 30 minutes**.

---

## Reproducibility

The full pipeline, including data preprocessing, model training, and evaluation, is reproducible using the provided scripts and notebooks. No proprietary tooling is required. 
The main Jupyter Notebook (**Virtuoso_pipeline**) used for conducting the experiments and searching the optimal parameters is deposited in the root folder of the GitHub repository. It is designed to be executed on Google Colab.

---

## Observations

* Gradient-boosted models (XGBoost, LightGBM, CatBoost) consistently outperform traditional Random Forest and DNN in both datasets.
* DNN shows notable improvement on CSE-CIC-IDS2018-WEB after balancing techniques.
* AUC-ROC values above 0.997 were observed for all models except the DNN on UNSW.

---

## Notes

* The use of SMOTE and class-weighting was crucial to handle dataset imbalance.
* Stratified 5-fold cross-validation was used for all evaluations.
