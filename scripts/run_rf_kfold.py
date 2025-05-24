"""
Random-Forest  │  5-fold Stratified CV  │  SMOTE on the training fold
Outputs eight metrics + ROC / PR curves exactly as used in the paper.

Author : VIRTUOSO project – May 2025
"""

import pandas as pd, numpy as np, matplotlib.pyplot as plt

from sklearn.compose       import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline      import Pipeline
from sklearn.ensemble      import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    matthews_corrcoef, roc_auc_score, average_precision_score,
    roc_curve, precision_recall_curve, auc
)
from imblearn.over_sampling import SMOTE


# ---------------------------------------------------------------------
def run_rf_kfold(X_path: str,
                 y_path: str,
                 prefix: str,
                 n_splits: int = 5,
                 sample_frac: float = 1.0) -> None:
    """
    Parameters
    ----------
    X_path, y_path : str
        CSV files produced by your preprocessing step
        (X = features, y = binary labels).
    prefix : str
        A short label used on plots and in log messages.
    n_splits : int
        Number of CV folds (default = 5).
    sample_frac : float
        Use < 1.0 to down-sample the very large UNSW dataset so the
        script finishes quickly on CPU (keeps class ratio).
    """

    # -----------------------------------------------------------------
    # 1 ── Load & optional sampling
    # -----------------------------------------------------------------
    X = pd.read_csv(X_path, low_memory=False)
    y = pd.read_csv(y_path).squeeze()

    if sample_frac < 1.0:
        idx = X.sample(frac=sample_frac, random_state=42).index
        X = X.loc[idx].reset_index(drop=True)
        y = y.loc[idx].reset_index(drop=True)

    # Identify categorical vs numerical columns
    cat_cols = list(X.select_dtypes('object').columns)
    num_cols = [c for c in X.columns if c not in cat_cols]

    # CV initialisation
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

    # Storage for metrics
    metrics = {m: [] for m in
               ['acc', 'prec', 'rec', 'f1', 'mcc', 'auc', 'prauc']}
    y_all, p_all = [], []

    # -----------------------------------------------------------------
    # 2 ── Cross-Validation loop
    # -----------------------------------------------------------------
    for fold, (tr_idx, va_idx) in enumerate(skf.split(X, y), start=1):
        X_tr, X_va = X.iloc[tr_idx], X.iloc[va_idx]
        y_tr, y_va = y.iloc[tr_idx], y.iloc[va_idx]

        # ⇒ Balance the training fold
        X_tr, y_tr = SMOTE(random_state=42).fit_resample(X_tr, y_tr)

        # Build preprocessing + model pipeline
        pipe = Pipeline([
            ('prep', ColumnTransformer([
                ('num', 'passthrough', num_cols),
                ('cat', OneHotEncoder(handle_unknown='ignore',
                                      sparse_output=True),
                 cat_cols)
            ])),
            ('rf', RandomForestClassifier(
                n_estimators=100,
                n_jobs=-1,
                random_state=42))
        ])

        pipe.fit(X_tr, y_tr)

        y_hat  = pipe.predict(X_va)
        y_prob = pipe.predict_proba(X_va)[:, 1]

        # accumulate for global ROC/PR
        y_all.extend(y_va)
        p_all.extend(y_prob)

        # ---- Metrics on this fold
        metrics['acc'  ].append(accuracy_score (y_va, y_hat))
        metrics['prec' ].append(precision_score(y_va, y_hat))
        metrics['rec'  ].append(recall_score   (y_va, y_hat))
        metrics['f1'   ].append(f1_score      (y_va, y_hat))
        metrics['mcc'  ].append(matthews_corrcoef(y_va, y_hat))
        metrics['auc'  ].append(roc_auc_score(y_va, y_prob))
        metrics['prauc'].append(average_precision_score(y_va, y_prob))

        print(f"✅ Fold {fold}/{n_splits} done.")

    # -----------------------------------------------------------------
    # 3 ── Aggregate & display
    # -----------------------------------------------------------------
    print(f"\n📊  {prefix}  —  Random Forest  ({n_splits}-fold CV)")
    for k in ['acc', 'prec', 'rec', 'f1', 'mcc']:
        print(f"{k.upper():8}: {np.mean(metrics[k]):.4f}"
              f" ± {np.std(metrics[k]):.4f}")
    print(f"AUC-ROC : {np.mean(metrics['auc']):.4f}")
    print(f"AUC-PR  : {np.mean(metrics['prauc']):.4f}")

    # Global ROC / PR curves
    fpr, tpr, _  = roc_curve             (y_all, p_all)
    prec, rec, _ = precision_recall_curve(y_all, p_all)

    plt.figure(figsize=(5, 4))
    plt.plot(fpr, tpr, label=f"AUC = {auc(fpr, tpr):.3f}")
    plt.plot([0, 1], [0, 1], linestyle='--', color='grey')
    plt.title(f"{prefix}  ROC (1)")
    plt.xlabel("False Positive Rate"); plt.ylabel("True Positive Rate")
    plt.grid(True); plt.legend(); plt.tight_layout(); plt.show()

    plt.figure(figsize=(5, 4))
    plt.plot(rec, prec, label=f"AUC = {auc(rec, prec):.3f}")
    plt.title(f"{prefix}  Precision-Recall (2)")
    plt.xlabel("Recall"); plt.ylabel("Precision")
    plt.grid(True); plt.legend(); plt.tight_layout(); plt.show()


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--X", required=True, help="Path to X CSV")
    p.add_argument("--y", required=True, help="Path to y CSV")
    p.add_argument("--prefix", default="UNSW-NB15")
    p.add_argument("--folds", type=int, default=5)
    p.add_argument("--sample", type=float, default=1.0)
    args = p.parse_args()
    run_rf_kfold(args.X, args.y, args.prefix, args.folds, args.sample)
