from injector import inject, Annotated

class IllyriadDBDao():
    @inject
    def __init__(self, metadata_table: Annotated[object, "MetadataTable"], players_table: Annotated[object, "PlayersTable"]):
        # TODO: Remove the Annotated
        print(f'Initializing {self.__class__.__name__}')
        self.metadata_table = metadata_table
        self.players_table = players_table

    def get_player_refresh_needed(self) -> bool:
        return bool(self.__get_metadata('REFRESH_PLAYERS'))

    def set_players_refreshed(self) -> None:
        response = self.metadata_table.update_item(
            Key={
                'partition_key_name': 'REFRESH_PLAYERS'
            },
            UpdateExpression="SET valuestring = :valuestring",
            ExpressionAttributeValues={
                ':valuestring': False
            },
            ReturnValues="UPDATED_NEW",
            ReturnConsumedCapacity="NONE",
        )
        assert not response['Attributes']['valuestring']

    def get_metadata_refresh_needed(self) -> bool:
        return bool(self.__get_metadata('REFRESH_METADATA'))

    def set_metadata_refreshed(self) -> None:
        response = self.metadata_table.update_item(
            Key={
                'partition_key_name': 'REFRESH_METADATA'
            },
            UpdateExpression="SET valuestring = :valuestring",
            ExpressionAttributeValues={
                ':valuestring': False
            },
            ReturnValues="UPDATED_NEW",
            ReturnConsumedCapacity="NONE",
        )
        assert not response['Attributes']['valuestring']

    def get_incoming_webhook_url(self) -> str:
        return self.__get_metadata('WAR_INCOMING_WEBHOOK_URL')
    
    def get_illyriad_towns_url(self) -> str:
        return self.__get_metadata('ILLYRIAD_TOWNS_URL')

    def __get_metadata(self, key_name: str) -> str:
        print(f'Getting metadata value for {key_name}')
        item = self.metadata_table.get_item(
            Key={
                'partition_key_name': key_name
            },
            ReturnConsumedCapacity='NONE'
        )
        return item['Item']['valuestring']
        
    def scan_players(self):
        print(f'Scanning players table')
        response = self.players_table.scan(
            Select='ALL_ATTRIBUTES',
            ReturnConsumedCapacity='NONE',
        )
        return response['Items']

    def update_player_latest_notif_id(self, player_id: int, latest_notif_id: str) -> None:
        print(f'Updating player {player_id} with latest notification id {latest_notif_id}')
        response = self.players_table.update_item(
            Key={
                'player_id': player_id
            },
            UpdateExpression="SET last_notification_id = :latest_notif_id",
            ExpressionAttributeValues={
                ':latest_notif_id': latest_notif_id
            },
            ReturnValues="UPDATED_NEW",
            ReturnConsumedCapacity="NONE",
        )
        assert response['Attributes']['last_notification_id'] == latest_notif_id
