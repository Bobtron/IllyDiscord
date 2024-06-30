from injector import inject

from cache.cache_interface import Cache
from aws.illyriad_db_dao import IllyriadDBDao

class MetadataCache(Cache):
    @inject
    def __init__(self, illyriad_db_dao: IllyriadDBDao):
        super().__init__(illyriad_db_dao)
        print(f'Initializing {self.__class__.__name__}')
        self.illyriad_towns_url = ''
        self.channel_to_webhook_url = {

        }

    def load(self, force: bool = False) -> None:
        if force or self.refresh_needed():
            self.__load_from_dao()

    def refresh_needed(self) -> bool:
        return self.illyriad_db_dao.get_metadata_refresh_needed()

    def __load_from_dao(self) -> None:
        self.illyriad_towns_url = self.illyriad_db_dao.get_illyriad_towns_url()
        self.channel_to_webhook_url['INCOMING_WEBHOOK_URL'] = self.illyriad_db_dao.get_incoming_webhook_url()
        # print(self.channel_to_webhook_url)
