# VIRTUOSO: Tables from the Paper



## Table 1: Cloud computing tools and compliance of SecOps principles

| Tool | Compliance Framework | Security Testing | Security Orchestration |
|------|----------------------|-------------------|------------------------|
| Jenkins | ✓ | ✓ | ✓ |
| GitLab | ✓ | ✓ | ✓ |
| Ansible | ✓ | - | ✓ |
| Terraform | ✓ | - | ✓ |
| Docker | - | ✓ | ✓ |
| Kubernetes | - | ✓ | ✓ |
| Prometheus | - | - | ✓ |
| ELK Stack | - | - | ✓ |

## Table 2: New Shared Responsibility Model under VIRTUOSO

| Security Domain | IaaS | PaaS | SaaS |
|-----------------|------|------|------|
| Data and Data Access | Shared | Shared | Shared |
| Application | User | User | Provider |
| Middleware | User | Shared | Provider |
| Operating Systems | Shared | Provider | Provider |
| Network | Shared | Provider | Provider |
| Virtual Environments | Shared | Provider | Provider |
| Physical Security | Provider | Provider | Provider |

## Table 3: Comparison of CSR Model and Deep Automation Security Layer

| Security Domain | Traditional CSR | VIRTUOSO CSR |
|-----------------|-----------------|--------------|
| Data and Data Access | User | Shared |
| Application | User | User (IaaS, PaaS), Provider (SaaS) |
| Middleware | User (IaaS), Provider (PaaS, SaaS) | Shared (IaaS, PaaS), Provider (SaaS) |
| Operating Systems | User (IaaS), Provider (PaaS, SaaS) | Shared (IaaS), Provider (PaaS, SaaS) |
| Network | Shared | Shared |
| Virtual Environments | Provider | Shared |
| Physical Security | Provider | Provider |

## Table 4: Performance Results of Machine Learning Algorithms

| Algorithm | Dataset | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-----------|---------|----------|-----------|--------|----------|---------|
| Random Forest (Weka) | UNSW-NB15 | 98.85% | 98.88% | 98.83% | 98.85 | 0.9975 |
| SVM (Weka) | UNSW-NB15 | 97.60% | 97.65% | 97.56% | 97.60 | 0.9945 |
| Naive Bayes (Weka) | UNSW-NB15 | 95.40% | 95.48% | 95.33% | 95.40 | 0.9855 |
| J48 (Weka) | UNSW-NB15 | 97.20% | 97.25% | 97.16% | 97.20 | 0.9925 |
| XGBoost | UNSW-NB15 | 99.82% | 99.85% | 99.80% | 99.82 | 0.9995 |
| LightGBM | UNSW-NB15 | 99.78% | 99.81% | 99.76% | 99.78 | 0.9993 |
| CatBoost | UNSW-NB15 | 99.80% | 99.83% | 99.78% | 99.80 | 0.9994 |
| DNN | UNSW-NB15 | 99.75% | 99.78% | 99.73% | 99.75 | 0.9992 |
| LSTM | UNSW-NB15 | 99.79% | 99.82% | 99.77% | 99.79 | 0.9994 |
| Random Forest (Weka) | CSE-CIC-IDS2018 | 99.00% | 99.03% | 98.98% | 99.00 | 0.9980 |
| SVM (Weka) | CSE-CIC-IDS2018 | 98.20% | 98.25% | 98.16% | 98.20 | 0.9960 |
| Naive Bayes (Weka) | CSE-CIC-IDS2018 | 96.50% | 96.57% | 96.44% | 96.50 | 0.9890 |
| J48 (Weka) | CSE-CIC-IDS2018 | 98.00% | 98.05% | 97.96% | 98.00 | 0.9950 |
| XGBoost | CSE-CIC-IDS2018 | 99.91% | 99.93% | 99.90% | 99.91 | 0.9998 |
| LightGBM | CSE-CIC-IDS2018 | 99.89% | 99.91% | 99.88% | 99.89 | 0.9997 |
| CatBoost | CSE-CIC-IDS2018 | 99.90% | 99.92% | 99.89% | 99.90 | 0.9997 |
| DNN | CSE-CIC-IDS2018 | 99.87% | 99.89% | 99.86% | 99.87 | 0.9996 |
| LSTM | CSE-CIC-IDS2018 | 99.88% | 99.90% | 99.87% | 99.88 | 0.9997 |

## Table 5: Comparison of VIRTUOSO with Existing Approaches

| Approach | Accuracy | FPR | Reference |
|----------|----------|-----|-----------|
| VIRTUOSO (XGBoost) | 99.91% | 0.07% | Current study |
| Deep Learning-based IDS | 98.80% | 0.65% | [85] |
| Unsupervised Deep Learning | 99.20% | 0.40% | [86] |
| Ensemble Learning IDS | 99.10% | 0.33% | [87] |
