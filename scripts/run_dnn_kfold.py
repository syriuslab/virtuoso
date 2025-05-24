"""
Balanced Deep Neural Network  │  5-fold CV  │  SMOTE + Class Weights
Architecture: [256→128→64] ReLU + BN + Dropout(0.5), Sigmoid output.
"""

import pandas as pd, numpy as np, matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.regularizers import l2
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    matthews_corrcoef, roc_auc_score, average_precision_score,
    roc_curve, precision_recall_curve, auc
)
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE

def run_dnn_kfold(X_path, y_path, prefix, n_splits=5, sample_frac=1.0):
    # 1. Load & sample
    X = pd.read_csv(X_path, low_memory=False)
    y = pd.read_csv(y_path).squeeze()
    if sample_frac < 1.0:
        idx = X.sample(frac=sample_frac, random_state=42).index
        X, y = X.loc[idx].reset_index(drop=True), y.loc[idx].reset_index(drop=True)

    # Encode categorical columns
    cat_cols = list(X.select_dtypes('object').columns)
    le = LabelEncoder()
    for c in cat_cols:
        X[c] = le.fit_transform(X[c])

    # Stratified 5-fold
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

    mets = {k:[] for k in ['acc','prec','rec','f1','mcc','auc','prauc']}
    y_all, p_all = [], []

    # Callbacks
    early = EarlyStopping(patience=10, restore_best_weights=True)
    reduce_lr = ReduceLROnPlateau(factor=0.1, patience=5, min_lr=1e-6)

    for f,(tr,va) in enumerate(skf.split(X,y), start=1):
        X_tr, y_tr = X.iloc[tr], y.iloc[tr]
        X_va, y_va = X.iloc[va], y.iloc[va]

        # Balance training with SMOTE
        X_tr, y_tr = SMOTE(random_state=42).fit_resample(X_tr, y_tr)

        # Compute class weights
        from sklearn.utils.class_weight import compute_class_weight
        weights = compute_class_weight('balanced', classes=np.unique(y_tr), y=y_tr)
        class_weights = dict(enumerate(weights))

        # Build model
        model = Sequential([
            Dense(256, activation='relu', kernel_regularizer=l2(0.01),
                  input_shape=(X_tr.shape[1],)),
            BatchNormalization(), Dropout(0.5),
            Dense(128, activation='relu', kernel_regularizer=l2(0.01)),
            BatchNormalization(), Dropout(0.5),
            Dense(64, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        model.compile(loss='binary_crossentropy', optimizer='adam')

        # Train
        model.fit(
            X_tr, y_tr, epochs=100, batch_size=64, verbose=0,
            validation_data=(X_va, y_va),
            callbacks=[early, reduce_lr],
            class_weight=class_weights
        )

        # Predict
        y_hat = (model.predict(X_va) > 0.5).astype(int).flatten()
        y_prob = model.predict(X_va).flatten()

        y_all.extend(y_va); p_all.extend(y_prob)
        mets['acc'].append(accuracy_score(y_va, y_hat))
        mets['prec'].append(precision_score(y_va, y_hat))
        mets['rec'].append(recall_score(y_va, y_hat))
        mets['f1'].append(f1_score(y_va, y_hat))
        mets['mcc'].append(matthews_corrcoef(y_va, y_hat))
        mets['auc'].append(roc_auc_score(y_va, y_prob))
        mets['prauc'].append(average_precision_score(y_va, y_prob))
        print(f"✅ Fold {f} done")

    # Summary
    print(f"\n📊 {prefix} — Balanced DNN ({n_splits}-fold CV)")
    for k in ['acc','prec','rec','f1','mcc']:
        print(f"{k.upper():8}: {np.mean(mets[k]):.4f} ± {np.std(mets[k]):.4f}")
    print(f"AUC-ROC : {np.mean(mets['auc']):.4f}")
    print(f"AUC-PR  : {np.mean(mets['prauc']):.4f}")

    # Global plots
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
    p.add_argument("--class_weight", action="store_true",
                   help="apply sklearn.compute_class_weight for DNN")
    args = p.parse_args()
    run_dnn_kfold(args.X, args.y, args.prefix, args.folds, args.sample)
