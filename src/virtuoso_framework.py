import os
from .deep_automation_layer.security_policy_enforcer import SecurityPolicyEnforcer
from .intelligent_security_layer.ml_engine import MLEngine
from .data_preprocessing.preprocess_UNSW_NB15 import preprocess_UNSW_NB15
from .data_preprocessing.preprocess_CSE_CIC_IDS2018 import preprocess_CSE_CIC_IDS2018

class VIRTUOSOFramework:
    def __init__(self, dataset_type, use_weka=False):
        self.dataset_type = dataset_type
        self.security_policy_enforcer = SecurityPolicyEnforcer(dataset_type)
        self.ml_engine = MLEngine(use_weka=use_weka)
        self.use_weka = use_weka

    def run(self, data_file_path):
        # Load and preprocess data
        if self.dataset_type == 'UNSW-NB15':
            X, y = preprocess_UNSW_NB15(data_file_path)
        elif self.dataset_type == 'CSE-CIC-IDS2018':
            X, y = preprocess_CSE_CIC_IDS2018(data_file_path)
        else:
            raise ValueError("Unsupported dataset type")

        if self.use_weka:
            # Use Weka configurations
            weka_config_path = os.path.join('src', 'weka_configs')
            self.ml_engine.load_weka_config(weka_config_path)

        # Train ML model
        self.ml_engine.train(X, y)

        # Apply security policies
        self.security_policy_enforcer.enforce_policies(X)

        # Make predictions
        predictions = self.ml_engine.predict(X)

        return predictions

    # ... additional methods ...
