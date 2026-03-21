from logging import config

from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.textSummarizer.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

DATA_INGESTION = "Data Ingestion stage"
DATA_TRANSFORMATION = "Data Transformation stage"
MODEL_TRAINER = "Model Trainer stage"
MODEL_EVALUATION = "Model Evaluation stage"

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
    
    ## Initiating the data transformation component
    try:
        logger.info(f"stage {DATA_TRANSFORMATION} initiated")
        data_transformation_pipeline=DataTransformationTrainingPipeline()
        data_transformation_pipeline.initiate_data_Transformation()
        logger.info(f"Stage {DATA_TRANSFORMATION} Completed")
    except Exception as e:
        logger.exception(e)
        raise e

    ## Initiating the model trainer component
    try:
        logger.info(f"stage {MODEL_TRAINER} initiated")
        model_trainer_pipeline=ModelTrainerTrainingPipeline()
        model_trainer_pipeline.initiate_model_trainer()
        logger.info(f"Stage {MODEL_TRAINER} Completed")
    except Exception as e:
        logger.exception(e)
        raise e
    
    ## Initiating the model evaluation component
    try:
        logger.info(f"stage {MODEL_EVALUATION} initiated")
        model_evaluation_pipeline=ModelEvaluationTrainingPipeline()
        model_evaluation_pipeline.initiate_model_evaluation()
        logger.info(f"Stage {MODEL_EVALUATION} Completed")
    except Exception as e:
        logger.exception(e)
        raise e

if __name__=="__main__":
    main()