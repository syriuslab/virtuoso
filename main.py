from src.virtuoso_framework import VIRTUOSOFramework
from src.utils import logger, config, check_dependencies

def main():
    try:
        check_dependencies()
        
        # Example with UNSW-NB15 dataset
        logger.info("Starting VIRTUOSO with UNSW-NB15 dataset")
        virtuoso_unsw = VIRTUOSOFramework('UNSW-NB15', use_weka=config['weka']['use_weka'])
        results_unsw = virtuoso_unsw.run(config['datasets']['UNSW-NB15']['path'])
        logger.info("Results for UNSW-NB15:")
        logger.info(results_unsw)

        # Example with CSE-CIC-IDS2018 dataset
        logger.info("Starting VIRTUOSO with CSE-CIC-IDS2018 dataset")
        virtuoso_cse = VIRTUOSOFramework('CSE-CIC-IDS2018', use_weka=config['weka']['use_weka'])
        results_cse = virtuoso_cse.run(config['datasets']['CSE-CIC-IDS2018']['path'])
        logger.info("Results for CSE-CIC-IDS2018:")
        logger.info(results_cse)

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)

if __name__ == "__main__":
    main()
