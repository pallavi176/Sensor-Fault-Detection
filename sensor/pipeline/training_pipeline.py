import os
import sys
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.components.data_ingestion import DataIngestion
from sensor.constants.s3_bucket import TRAINING_BUCKET_NAME
from sensor.constants.training_pipeline import SAVED_MODEL_DIR

class TrainPipeline:

    is_pipeline_running=False

    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except  Exception as e:
            raise  SensorException(e, sys)

    def run_pipeline(self):
        try:
            
            TrainPipeline.is_pipeline_running=True
            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()
        except  Exception as e:
            TrainPipeline.is_pipeline_running = False
            raise  SensorException(e,sys)