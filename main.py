from summarize_text.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from summarize_text.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
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



STAGE_NAME = "Data Validation"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=======================x")


except Exception as e:
    logger.exception(e)
    raise e