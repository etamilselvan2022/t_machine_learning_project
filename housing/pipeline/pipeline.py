from housing.config.configuration import Configuration
from housing.exception import HousingException
from housing.entity.artifact_entity import DataIngestionArtifact
import os,sys
from housing.component.data_ingestion import DataIngestion




class Pipeline:

    def __init__(self,config:Configuration=Configuration())-> None:
        try:
            self.config=config
        except Exception as e:
            raise HousingException(e,sys) from e

    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            data_ingestion_artifact=DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config()).initiate_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e        

    def run_pipeline(self)-> DataIngestionArtifact:
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            print(f'data_ingestion_artifact:{data_ingestion_artifact}')
        except Exception as e:
            raise HousingException(e,sys) from e       
