VIRTUOSO: A Multilayer Architecture for Cloud Security

Overview

VIRTUOSO (Virtuous Security On-machine based) is an advanced multilayer framework designed to enhance security in cloud computing environments. It leverages state-of-the-art Machine Learning (ML) and Artificial Intelligence (AI) techniques, integrating them with industry-leading security practices and SecOps principles.
Key Features

Deep Automation Security Layer for implementing best security practices
Intelligent Security Layer utilizing advanced ML algorithms
Support for multiple ML models: XGBoost, LightGBM, CatBoost, Deep Neural Networks, and LSTM
Comprehensive analysis using UNSW-NB15 and CSE-CIC-IDS2018 datasets
Scalable architecture suitable for various cloud service models (IaaS, PaaS, SaaS)

Installation

Clone the repository:

- git clone https://github.com/syriuslab/virtuoso.git


Set up a virtual environment (optional but recommended):
- cd virtuoso
- python -m venv venv
- source venv/bin/activate  # On Windows use `venv\Scripts\activate`
- pip install -r requirements.txt

Install the required packages:
- pip install -r requirements.txt

Install the project in editable mode:
- pip install -e .

Configuration

Navigate to the config directory.
Open config.yaml and adjust the settings as needed:

Set the correct paths for the UNSW-NB15 and CSE-CIC-IDS2018 datasets.
Modify the parameters for each ML model if necessary.


Usage

Ensure your dataset files are in the correct location as specified in config.yaml.
Run the main script:

- python src/main.py


The script will load the data, preprocess it, train the models, and output the evaluation metrics for each model on both datasets.


Project Structure

src/: Source code

data/: Data loading and preprocessing
models/: Implementation of various ML models
utils/: Utility functions (configuration, logging, metrics)
main.py: Main execution script


tests/: Unit tests
config/: Configuration files
requirements.txt: List of Python dependencies
setup.py: Setup script for the project

Running Tests
To run the unit tests:

- python -m unittest discover tests

Datasets
VIRTUOSO uses two primary datasets:

UNSW-NB15: A comprehensive dataset for network intrusion detection systems.
CSE-CIC-IDS2018: A diverse dataset containing benign and the most up-to-date common attacks.

Ensure you have these datasets downloaded and their paths correctly specified in the configuration file.
Contributing
We welcome contributions to VIRTUOSO! Please follow these steps:

Fork the repository.
Create a new branch for your feature (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a Pull Request.


Acknowledgments

UNSW-NB15 Dataset: https://research.unsw.edu.au/projects/unsw-nb15-dataset
CSE-CIC-IDS2018 Dataset: https://www.unb.ca/cic/datasets/ids-2018.html
