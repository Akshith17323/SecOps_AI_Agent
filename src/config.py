import os
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Base project paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
MODELS_DIR = os.path.join(PROJECT_ROOT, "models")
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

# UCI Machine Learning Repository Dataset ID for RT-IoT2022
UCI_DATASET_ID = 942

# Default local dataset file path
DATASET_PATH = os.path.join(DATA_DIR, "RT_IOT2022.csv")


def ensure_dataset() -> str:
    """
    Returns the absolute path to data/RT_IOT2022.csv.
    If not found locally, automatically fetches it via ucimlrepo
    and saves it to data/RT_IOT2022.csv.
    """
    if os.path.exists(DATASET_PATH):
        return DATASET_PATH

    logger.info(f"Local dataset not found at {DATASET_PATH}. Fetching dataset {UCI_DATASET_ID} via ucimlrepo...")
    try:
        from ucimlrepo import fetch_ucirepo
        dataset = fetch_ucirepo(id=UCI_DATASET_ID)
        df = pd.concat([dataset.data.features, dataset.data.targets], axis=1)
        df.to_csv(DATASET_PATH, index=False)
        logger.info(f"Dataset successfully fetched and saved to: {DATASET_PATH}")
        return DATASET_PATH
    except Exception as e:
        logger.error(f"Failed to fetch dataset from ucimlrepo: {e}")
        raise


# Ensure dataset exists and export path
DATASET_FILE = ensure_dataset()
