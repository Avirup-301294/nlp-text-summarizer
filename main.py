from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

DATA_INGESTION = "Data Ingestion stage"

def main():
    ## Initiating the data ingestion training pipeline
    try:
        logger.info(f"stage {DATA_INGESTION} initiated")
        data_ingestion_pipeline=DataIngestionTrainingPipeline()
        data_ingestion_pipeline.initiate_data_ingestion()
        logger.info(f"Stage {DATA_INGESTION} Completed")
    except Exception as e:
        logger.exception(e)
        raise e

if __name__=="__main__":
    main()