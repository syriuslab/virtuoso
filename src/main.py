import logging
from data.data_loader import load_data
from data.preprocessor import preprocess_data
from models.xgboost_model import XGBoostModel
from models.lightgbm_model import LightGBMModel
from models.catboost_model import CatBoostModel
from models.dnn_model import DNNModel
from models.lstm_model import LSTMModel
from utils.config import load_config
from utils.metrics import evaluate_model

def main():
    config = load_config()
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Loading data...")
    unsw_data, cse_data = load_data(config['unsw_path'], config['cse_path'])

    logger.info("Preprocessing data...")
    unsw_result, cse_result = preprocess_data(unsw_data, cse_data)
    
    datasets = [
        ("UNSW-NB15", unsw_result),
        ("CSE-CIC-IDS2018", cse_result)
    ]

    models = [
        XGBoostModel(config['xgboost_params']),
        LightGBMModel(config['lightgbm_params']),
        CatBoostModel(config['catboost_params']),
        DNNModel(config['dnn_params']),
        LSTMModel(config['lstm_params'])
    ]

    for dataset_name, (X_train, X_test, y_train, y_test) in datasets:
        logger.info(f"Processing {dataset_name} dataset")
        for model in models:
            logger.info(f"Training {model.__class__.__name__}...")
            model.train(X_train, y_train)
            
            logger.info(f"Evaluating {model.__class__.__name__}...")
            y_pred = model.predict(X_test)
            metrics = evaluate_model(y_test, y_pred)
            logger.info(f"Metrics for {model.__class__.__name__} on {dataset_name}: {metrics}")

if __name__ == "__main__":
    main()
