from injector import inject

class IllyriadDBDao():
    @inject
    def __init__(self, dynamodb_res):
        print(f'Initializing {self.__class__.__name__}')
        self.dynamodb_res = dynamodb_res
        self.metadata_table = dynamodb_res.Table('Illyriad-Metadata-Prod')
        self.players_table = dynamodb_res.Table('Illyriad-Notifications-Prod')

    def get_player_refresh_needed(self) -> bool:
        return bool(self.__get_metadata('REFRESH_PLAYERS'))

    def get_metadata_refresh_needed(self) -> bool:
        return bool(self.__get_metadata('REFRESH_METADATA'))

    def get_incoming_webhook_url(self) -> str:
        return self.__get_metadata('WAR_INCOMING_WEBHOOK_URL')
    
    def get_illyriad_towns_url(self) -> str:
        return self.__get_metadata('ILLYRIAD_TOWNS_URL')

    def __get_metadata(self, key_name: str) -> str:
        item = self.metadata_table.get_item(
            Key={
                'partition_key_name': key_name
            },
            ReturnConsumedCapacity='NONE'
        )
        return item['Item']['valuestring']
        
    def scan_players(self):
        response = self.players_table.scan(
            Select='ALL_ATTRIBUTES',
            ReturnConsumedCapacity='NONE',
        )
        return response['Items']

    def update_player_latest_notif_id(self, player_id: int, latest_notif_id: int) -> None:
        response = self.players_table.update_item(
            Key={
                'player_id': player_id
            },
            UpdateExpression="SET latest_notifications_id = :latest_notif_id",
            ExpressionAttributeValues={
                ':latest_notif_id': int(latest_notif_id)
            },
            ReturnValues="UPDATED_NEW",
            ReturnConsumedCapacity="NONE",
        )
        # print(response)
        assert response['Attributes']['latest_notifications_id'] == latest_notif_id
