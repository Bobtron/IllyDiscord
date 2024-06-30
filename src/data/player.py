
class Player():
    def __init__(self, player_id: int, discord_user_id: int, latest_notif_id: int, notif_api_key: str):
        self.player_id = player_id
        self.discord_user_id = discord_user_id
        self.latest_notif_id = latest_notif_id
        self.notif_api_key = notif_api_key

    def __str__(self):
        return self.__to_string()
    def __unicode__(self):
        return self.__to_string()
    def __repr__(self):
        return self.__to_string()

    def __to_string(self) -> str:
        return f"Player(player_id={self.player_id}, discord_user_id={self.discord_user_id}, latest_notif_id={self.latest_notif_id}, notif_api_key={self.notif_api_key})"