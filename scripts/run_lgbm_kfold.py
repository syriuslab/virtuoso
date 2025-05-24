"""
LightGBM  │  5-fold Stratified CV  │  L1/L2 regularization
"""

import pandas as pd, numpy as np, matplotlib.pyplot as plt
import lightgbm as lgb
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    matthews_corrcoef, roc_auc_score, average_precision_score,
    roc_curve, precision_recall_curve, auc
)
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE

def run_lgbm_kfold(X_path, y_path, prefix, n_splits=5, sample_frac=1.0):
    # Load
    X = pd.read_csv(X_path, low_memory=False)
    y = pd.read_csv(y_path).squeeze()
    if sample_frac < 1.0:
        idx = X.sample(frac=sample_frac, random_state=42).index
        X, y = X.loc[idx].reset_index(drop=True), y.loc[idx].reset_index(drop=True)

    # Encode categoricals
    cat_cols = X.select_dtypes('object').columns
    le = LabelEncoder()
    for c in cat_cols:
        X[c] = le.fit_transform(X[c])

    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    mets = {k:[] for k in ['acc','prec','rec','f1','mcc','auc','prauc']}
    y_all, p_all = [], []

    # Class weight for imbalance
    pos_weight = sum(y==0)/sum(y==1)

    for f,(tr,va) in enumerate(skf.split(X,y), start=1):
        X_tr, X_va = X.iloc[tr], X.iloc[va]
        y_tr, y_va = y.iloc[tr], y.iloc[va]
        X_tr, y_tr = SMOTE(random_state=42).fit_resample(X_tr,y_tr)

        model = lgb.LGBMClassifier(
            n_estimators=100, num_leaves=31,
            learning_rate=0.1, max_depth=6,
            lambda_l1=0.1, lambda_l2=0.1,
            scale_pos_weight=pos_weight,
            random_state=42, n_jobs=-1
        )
        model.fit(X_tr,y_tr)

        y_hat = model.predict(X_va)
        y_prob = model.predict_proba(X_va)[:,1]
        y_all.extend(y_va); p_all.extend(y_prob)

        mets['acc'].append(accuracy_score(y_va,y_hat))
        mets['prec'].append(precision_score(y_va,y_hat))
        mets['rec'].append(recall_score(y_va,y_hat))
        mets['f1'].append(f1_score(y_va,y_hat))
        mets['mcc'].append(matthews_corrcoef(y_va,y_hat))
        mets['auc'].append(roc_auc_score(y_va,y_prob))
        mets['prauc'].append(average_precision_score(y_va,y_prob))
        print(f"✅ Fold {f} done")

    # Summary
    print(f"\n📊 {prefix} — LightGBM ({n_splits}-fold CV)")
    for k in ['acc','prec','rec','f1','mcc']:
        print(f"{k.upper():8}: {np.mean(mets[k]):.4f} ± {np.std(mets[k]):.4f}")
    print(f"AUC-ROC : {np.mean(mets['auc']):.4f}")
    print(f"AUC-PR  : {np.mean(mets['prauc']):.4f}")

    fpr,tpr,_  = roc_curve(y_all,p_all)
    prec,rec,_ = precision_recall_curve(y_all,p_all)

    plt.figure(figsize=(5,4))
    plt.plot(fpr,tpr,label=f"AUC={auc(fpr,tpr):.3f}")
    plt.plot([0,1],[0,1],'--',c='grey')
    plt.title(f"{prefix} ROC (1)")
    plt.xlabel("FPR"); plt.ylabel("TPR")
    plt.legend(); plt.grid(); plt.show()

    plt.figure(figsize=(5,4))
    plt.plot(rec,prec,label=f"AUC={auc(rec,prec):.3f}")
    plt.title(f"{prefix} PR (2)")
    plt.xlabel("Recall"); plt.ylabel("Precision")
    plt.legend(); plt.grid(); plt.show()

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--X", required=True)
    p.add_argument("--y", required=True)
    p.add_argument("--prefix", default="UNSW-NB15")
    p.add_argument("--folds", type=int, default=5)
    p.add_argument("--sample", type=float, default=1.0)
    args = p.parse_args()
    run_lgbm_kfold(args.X, args.y, args.prefix, args.folds, args.sample)
