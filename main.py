from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline
import os

if __name__=="__main__":
    # mongodb_client = MongoDBClient()
    # print("Collection names: ", mongodb_client.database.list_collection_names())
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()