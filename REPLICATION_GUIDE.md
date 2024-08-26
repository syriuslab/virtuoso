# Guide to Replicate VIRTUOSO Experiments

This guide provides step-by-step instructions to replicate the experiments described in the VIRTUOSO paper.

## Prerequisites

- Python 3.8+
- Weka 3.8.5
- Datasets: UNSW-NB15 and CSE-CIC-IDS2018 (download links in the paper)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/syriuslab/virtuoso.git
   cd virtuoso
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Download the datasets and place them in a `data` folder in the project root.

## Running the Experiments

1. Preprocess the data:
   ```
   python src/data_preprocessing/preprocess_UNSW-NB15.py
   python src/data_preprocessing/preprocess_CSE_CIC_IDS2018.py
   ```

2. Run Weka experiments:
   ```
   java -jar weka.jar -main weka.Run .RF -t data/UNSW-NB15_processed.arff
   ```
   (Repeat for other Weka models and datasets)

3. Run Python experiments:
   ```
   python src/main.py
   ```

4. Analyze results:
   ```
   python src/analyze_results.py
   ```

For detailed explanations of each step, refer to the comments in the respective Python scripts.
