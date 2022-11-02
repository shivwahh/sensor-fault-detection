from datetime import datetime
import os
from sensor.constant.training_pipeline import PIPELINE

class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime