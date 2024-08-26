import yaml
import logging
import sys

def load_config(config_path='config.yaml'):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("virtuoso.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger('VIRTUOSO')

def check_dependencies():
    required_packages = ['pandas', 'numpy', 'scikit-learn', 'xgboost', 'lightgbm', 'tensorflow']
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        raise ImportError(f"Missing required packages: {', '.join(missing_packages)}")

logger = setup_logging()
config = load_config()
