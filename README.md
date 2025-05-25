## VIRTUOSO 🛡️

**VIRTUOSO** (Virtuous Security On-machine based) is an advanced multilayer framework designed to enhance security in cloud computing environments. It leverages state-of-the-art Machine Learning (ML) and Artificial Intelligence (AI) techniques, integrating them with industry-leading security practices and SecOps principles.
VIRTUOSO is a pure-Python framework that implements and evaluates five state-of-the-art machine-learning models over two large-scale IDS benchmarks—**UNSW-NB15** (real network traffic) and **CSE-CIC-IDS2018** (web-attack subset). All results in our paper can be reproduced in under 30 minutes per model on a free Google Colab T4 session.

---

## Key Features

- Deep Automation Security Layer for implementing best security practices


- Intelligent Security Layer utilizing advanced ML algorithms


- Support for multiple ML models: XGBoost, LightGBM, CatBoost and Deep Neural Networks


- Comprehensive analysis using UNSW-NB15 and CSE-CIC-IDS2018 datasets


- Scalable architecture suitable for various cloud service models (IaaS, PaaS, SaaS)


- Consideration for post-quantum era security challenges



* **Five classifiers**

  * **Baseline**: Random Forest
  * **Ensembles**: XGBoost, LightGBM, CatBoost
  * **Deep Net**: Balanced DNN (SMOTE + class-weight)

* **Two datasets**

  * **UNSW-NB15** (700 001 flows, 49 features, real-world)
  * **CSE-CIC-IDS2018-Web** (118 652 flows, 60 features, simulated HTTP attacks)

* **Rigorous evaluation**

  * 5-fold **stratified CV** (seed = 42, shuffle=True)
  * **SMOTE** on each training fold to address class imbalance
  * **Eight metrics**: Accuracy, Precision, Recall, F1-Score, MCC, AUC-ROC, AUC-PR, FPR & FNR
  * Global **ROC** & **PR** curves for each model

* **Reproducible & portable**

  * Runs in **< 30 min** per model on Colab T4 (≤ 8 GB RAM)
  * Identical behavior on commodity cloud instances
    (e.g. AWS g4dn.xlarge, Azure NC4as\_T4\_v3, GCP n1-standard-4 + T4)

---

## Repository Structure

```
virtuoso/
├── config.yaml               ← Dataset paths & hyperparameters  
├── main.py                   ← Unified CLI entry point  
├── README.md                 ← This file  
├── REPLICATION_GUIDE.md      ← Step-by-step reproduction instructions  
├── TABLES_PAPER.md           ← Markdown version of Table 4  
├── EXPERIMENT_LOG.md         ← Detailed runtimes & logs  
├── requirements.txt          ← Python dependencies  
└── scripts/  
    ├── run_rf_kfold.py       ← Random Forest  
    ├── run_xgb_kfold.py      ← XGBoost  
    ├── run_lgbm_kfold.py     ← LightGBM  
    ├── run_catboost_kfold.py ← CatBoost (CPU)  
    └── run_dnn_kfold.py      ← Balanced DNN  
```

---

## Quickstart

1. **Install dependencies**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Prepare data**
   Download or generate preprocessed CSVs and place them in `data/`:

   ```
   data/UNSW_X.csv      data/UNSW_y.csv
   data/IDS_X_web.csv   data/IDS_y_web.csv
   ```

3. **Run a model**

   ```bash
   # Example: XGBoost on UNSW-NB15
   python main.py --model xgb --dataset UNSW-NB15
   ```

   This will:

   * Perform **5-fold stratified CV** with SMOTE on each training fold
   * Compute and display **mean ± std** for all eight evaluation metrics
   * Plot **global ROC** & **Precision-Recall** curves

4. **Batch execution**
   To run all five models on both datasets:

   ```bash
   for m in rf xgb lgbm catboost dnn; do
     python main.py --model $m --dataset UNSW-NB15
     python main.py --model $m --dataset CSE-CIC-IDS2018

---

## Detailed Replication

See **REPLICATION\_GUIDE.md** for:

* Full environment setup
* Data acquisition & preprocessing
* Exact command lines & expected outputs

---

## Experiment Log & Timings

All runtime measurements, hardware details, and key observations are recorded in **EXPERIMENT\_LOG.md**.

---

