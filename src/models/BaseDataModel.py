from helpers.config import get_settings , Settings

class BaseDataModel:
    def __init__(self , db_client ):
        self.db_client = db_client
        self.settings = get_settings()
        # self.collection_name = self.settings.get('collection_name', 'default_collection')
        # self.collection = self.db_client[self.collection_name]