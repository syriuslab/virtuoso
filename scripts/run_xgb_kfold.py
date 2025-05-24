"""
XGBoost  │  5-fold Stratified CV  │  SMOTE on training fold
Computes 8 metrics + ROC/PR curves as per paper.
"""

import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    matthews_corrcoef, roc_auc_score, average_precision_score,
    roc_curve, precision_recall_curve, auc
)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE

def run_xgb_kfold(X_path, y_path, prefix, n_splits=5, sample_frac=1.0):
    # Load data
    X = pd.read_csv(X_path, low_memory=False)
    y = pd.read_csv(y_path).squeeze()
    if sample_frac < 1.0:
        idx = X.sample(frac=sample_frac, random_state=42).index
        X, y = X.loc[idx].reset_index(drop=True), y.loc[idx].reset_index(drop=True)

    cat_cols = list(X.select_dtypes('object').columns)
    num_cols = [c for c in X.columns if c not in cat_cols]
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

    mets = {k: [] for k in ['acc','prec','rec','f1','mcc','auc','prauc']}
    y_all, p_all = [], []

    for fold, (tr, va) in enumerate(skf.split(X, y), start=1):
        X_tr, y_tr = X.iloc[tr], y.iloc[tr]
        X_va, y_va = X.iloc[va], y.iloc[va]
        X_tr, y_tr = SMOTE(random_state=42).fit_resample(X_tr, y_tr)

        pipe = Pipeline([
            ('prep', ColumnTransformer([
                ('num', 'passthrough', num_cols),
                ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=True), cat_cols)
            ])),
            ('xgb', XGBClassifier(
                n_estimators=100, learning_rate=0.1, max_depth=6,
                use_label_encoder=False, eval_metric='logloss',
                random_state=42, n_jobs=-1))
        ])

        pipe.fit(X_tr, y_tr)
        y_hat = pipe.predict(X_va)
        y_prob = pipe.predict_proba(X_va)[:,1]

        y_all.extend(y_va); p_all.extend(y_prob)
        mets['acc'].append(accuracy_score(y_va, y_hat))
        mets['prec'].append(precision_score(y_va, y_hat))
        mets['rec'].append(recall_score(y_va, y_hat))
        mets['f1'].append(f1_score(y_va, y_hat))
        mets['mcc'].append(matthews_corrcoef(y_va, y_hat))
        mets['auc'].append(roc_auc_score(y_va, y_prob))
        mets['prauc'].append(average_precision_score(y_va, y_prob))
        print(f"✅ Fold {fold} done")

    # Summary
    print(f"\n📊 {prefix} — XGBoost ({n_splits}-fold CV)")
    for k in ['acc','prec','rec','f1','mcc']:
        print(f"{k.upper():8}: {np.mean(mets[k]):.4f} ± {np.std(mets[k]):.4f}")
    print(f"AUC-ROC : {np.mean(mets['auc']):.4f}")
    print(f"AUC-PR  : {np.mean(mets['prauc']):.4f}")

    fpr,tpr,_  = roc_curve(y_all, p_all)
    prec,rec,_ = precision_recall_curve(y_all, p_all)

    # ROC
    plt.figure(figsize=(5,4))
    plt.plot(fpr,tpr,label=f"AUC={auc(fpr,tpr):.3f}")
    plt.plot([0,1],[0,1],'--',c='grey')
    plt.title(f"{prefix} ROC (1)")
    plt.xlabel("FPR"); plt.ylabel("TPR")
    plt.legend(); plt.grid(); plt.show()

    # PR
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
    run_xgb_kfold(args.X, args.y, args.prefix, args.folds, args.sample)
