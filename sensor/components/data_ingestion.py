import os
import sys

from pandas import DataFrame
from sklearn.model_selection import train_test_split

from sensor.constant.training_pipeline import SCHEMA_DROP_COLS, SCHEMA_FILE_PATH
from sensor.data_access.sensor_data import SensorData
from sensor.entity.artifact_entity import DataInge
