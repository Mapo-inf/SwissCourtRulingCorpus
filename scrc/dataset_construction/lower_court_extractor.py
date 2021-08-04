import configparser
from typing import Optional, Any

from root import ROOT_DIR
from scrc.utils.abstract_extractor import AbstractExtractor
import pandas as pd

class LowerCourtExtractor(AbstractExtractor):
    """
    Extracts the lower courts from the header section
    """

    def __init__(self, config: dict):
        super().__init__(config, function_name='lower_court_extracting_functions', col_name='lower_court')

    def getDatabaseSelectionString(self, spider, lang) -> str:
        """Returns the `where` clause of the select statement for the entries to be processed by extractor"""
        return f"spider='{spider}' AND header IS NOT NULL AND header <> ''"

    def getRequiredData(self, series) -> Any:
        return series['header']

    def checkConditionBeforeProcess(self, spider: str, data: Any, namespace: dict) -> bool:
        """Override if data has to conform to a certain condition before processing. 
        e.g. data is required to be present for analysis"""
        return bool(data)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read(ROOT_DIR / 'config.ini')  # this stops working when the script is called from the src directory!

    lower_court_extractor = LowerCourtExtractor(config)
    lower_court_extractor.processed_file_path = lower_court_extractor.data_dir / "spiders_lower_court_extracted.txt"
    lower_court_extractor.loggerInfo = {
        'start': 'Started extracting lower court informations', 
        'finished': 'Finished extracting lower court informations', 
        'start_spider': 'Started extracting lower court informations for spider', 
        'finish_spider': 'Finished extracting lower court informations for spider', 
        'saving': 'Saving chunk of lower court informations',
        'processing_one': 'Extracting lower court informations from',
        'no_functions': 'Not extracting lower court informations.'
        }
    lower_court_extractor.start()