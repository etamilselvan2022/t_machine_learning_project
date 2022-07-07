from housing.exception import HousingException
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
import os,sys
try:
    data_ingestion_artifact=Pipeline().run_pipeline()
    print(data_ingestion_artifact)
except Exception as e:
    raise HousingException(e,sys) from e    
