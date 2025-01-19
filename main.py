from summarize_text.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from summarize_text.logging import logger



STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=======================x")


except Exception as e:
    logger.exception(e)
    raise e

