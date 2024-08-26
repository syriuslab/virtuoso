import os
from data_preprocessing.preprocess_UNSW_NB15 import preprocess_UNSW_NB15
from data_preprocessing.preprocess_CSE_CIC_IDS2018 import preprocess_CSE_CIC_IDS2018
from deep_automation_layer.security_policy_enforcer import SecurityPolicyEnforcer
from intelligent_security_layer.ml_engine import MLEngine

class VIRTUOSOFramework:
    def __init__(self, dataset_type, use_weka=False):
        self.dataset_type = dataset_type
        self.use_weka = use_weka
        self.security_policy_enforcer = SecurityPolicyEnforcer()
        self.ml_engine = MLEngine(use_weka=use_weka)

    def run(self, data_file_path):
        # Preprocess data
        if self.dataset_type == 'UNSW-NB15':
            X, y = preprocess_UNSW_NB15(data_file_path)
        elif self.dataset_type == 'CSE-CIC-IDS2018':
            X, y = preprocess_CSE_CIC_IDS2018(data_file_path)
        else:
            raise ValueError("Unsupported dataset type")

        # Apply security policies
        X_secure = self.security_policy_enforcer.enforce_policies(X)

        # Train and evaluate model
        results = self.ml_engine.train_and_evaluate(X_secure, y)

        return results

# Example usage
if __name__ == "__main__":
    virtuoso = VIRTUOSOFramework('UNSW-NB15', use_weka=False)
    results = virtuoso.run('path/to/UNSW-NB15_dataset.csv')
    print(results)
