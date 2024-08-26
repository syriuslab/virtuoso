from ..data_preprocessing.common_preprocessing import load_data
from ..data_preprocessing.preprocess_UNSW_NB15 import preprocess_UNSW_NB15
from ..data_preprocessing.preprocess_CSE_CIC_IDS2018 import preprocess_CSE_CIC_IDS2018

class SecurityPolicyEnforcer:
    def __init__(self, dataset_type):
        self.dataset_type = dataset_type

    def load_and_preprocess_data(self, file_path):
        if self.dataset_type == 'UNSW-NB15':
            return preprocess_UNSW_NB15(file_path)
        elif self.dataset_type == 'CSE-CIC-IDS2018':
            return preprocess_CSE_CIC_IDS2018(file_path)
        else:
            raise ValueError("Unsupported dataset type")

    # ... rest of the class implementation ...
