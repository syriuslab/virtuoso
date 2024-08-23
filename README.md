## VIRTUOSO 🛡️

[![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

VIRTUOSO (Virtuous Security On-machine based) is an advanced multilayer framework designed to enhance security in cloud computing environments. It leverages state-of-the-art Machine Learning (ML) and Artificial Intelligence (AI) techniques, integrating them with industry-leading security practices and SecOps principles.

## 🚀 Features

- Deep Automation Security Layer for implementing best security practices
- Intelligent Security Layer utilizing advanced ML algorithms
- Support for multiple ML models: XGBoost, LightGBM, CatBoost, Deep Neural Networks, and LSTM
- Comprehensive analysis using UNSW-NB15 and CSE-CIC-IDS2018 datasets
- Scalable architecture suitable for various cloud service models (IaaS, PaaS, SaaS)

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/syriuslab/virtuoso.git
   cd virtuoso
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the project in editable mode:
   ```bash
   pip install -e .
   ```

## ⚙️ Configuration

1. Navigate to the `config` directory.
2. Open `config.yaml` and adjust the settings as needed:
   - Set the correct paths for the UNSW-NB15 and CSE-CIC-IDS2018 datasets.
   - Modify the parameters for each ML model if necessary.

## 🖥️ Usage

1. Ensure your dataset files are in the correct location as specified in `config.yaml`.
2. Run the main script:
   ```bash
   python src/main.py
   ```
3. The script will load the data, preprocess it, train the models, and output the evaluation metrics for each model on both datasets.

## 📁 Project Structure

```
virtuoso/
│
├── src/
│   ├── data/
│   │   ├── data_loader.py
│   │   └── preprocessor.py
│   ├── models/
│   │   ├── xgboost_model.py
│   │   ├── lightgbm_model.py
│   │   ├── catboost_model.py
│   │   ├── dnn_model.py
│   │   └── lstm_model.py
│   ├── utils/
│   │   ├── config.py
│   │   └── metrics.py
│   └── main.py
│
├── tests/
│   ├── test_data_loader.py
│   ├── test_preprocessor.py
│   └── test_models.py
│
├── config/
│   └── config.yaml
│
├── requirements.txt
├── setup.py
└── README.md
```

## 🧪 Running Tests

To run the unit tests:

```bash
python -m unittest discover tests
```

## 📊 Datasets

VIRTUOSO uses two primary datasets:

1. [UNSW-NB15](https://research.unsw.edu.au/projects/unsw-nb15-dataset): A comprehensive dataset for network intrusion detection systems.
2. [CSE-CIC-IDS2018](https://www.unb.ca/cic/datasets/ids-2018.html): A diverse dataset containing benign and the most up-to-date common attacks.

Ensure you have these datasets downloaded and their paths correctly specified in the configuration file.

## 🤝 Contributing

We welcome contributions to VIRTUOSO! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/AmazingFeature`.
3. Make your changes and commit them: `git commit -m 'Add some AmazingFeature'`.
4. Push to the branch: `git push origin feature/AmazingFeature`.
5. Open a pull request.



## 📞 Contact

syriuscloudarchitect@gmail.com

Project Link: [https://github.com/syriuslab/virtuoso](https://github.com/syriuslab/virtuoso)

## 🙏 Acknowledgments

- All contributors who have helped shape VIRTUOSO
