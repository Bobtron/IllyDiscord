
from aws.illyriad_db_dao import IllyriadDBDao

class Cache():
    def __init__(self, illyriad_db_dao: IllyriadDBDao):
        print(f'Initializing {self.__class__.__name__}')
        self.illyriad_db_dao = illyriad_db_dao

    def load(self, force: bool = False) -> None:
        raise NotImplementedError()

    def get_refresh_needed(self) -> bool:
        raise NotImplementedError()
