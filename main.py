#!/usr/bin/env python3
"""
CLI wrapper for running any of the 5 k-fold scripts:

Example:
    python main.py --model xgb --dataset UNSW-NB15
"""

import argparse
import subprocess
import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).parent
with open(ROOT / "config.yaml", "r") as f:
    CFG = yaml.safe_load(f)

# mapping from short key to script path
SCRIPTS = {
    "rf":       "scripts/run_rf_kfold.py",
    "xgb":      "scripts/run_xgb_kfold.py",
    "lgbm":     "scripts/run_lgbm_kfold.py",
    "catboost": "scripts/run_catboost_kfold.py",
    "dnn":      "scripts/run_dnn_kfold.py",
}

def run(model: str, dataset: str):
    model = model.lower()
    script = ROOT / SCRIPTS[model]
    X = CFG["datasets"][dataset]["X_path"]
    y = CFG["datasets"][dataset]["y_path"]
    cmd = [
        sys.executable, str(script),
        "--X", X, "--y", y,
        "--prefix", dataset,
        "--folds", str(CFG["cv"]["n_splits"])
    ]
    if model == "dnn" and CFG["cv"]["class_weight_dnn"]:
        cmd += ["--class_weight"]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Run VIRTUOSO k-fold scripts")
    p.add_argument("--model", required=True,
                   choices=SCRIPTS.keys(),
                   help="Model to run")
    p.add_argument("--dataset", required=True,
                   choices=CFG["datasets"].keys(),
                   help="Dataset key")
    args = p.parse_args()
    run(args.model, args.dataset)
