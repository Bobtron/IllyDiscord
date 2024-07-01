from typing import List

from data.notification import Notification
from data.player import Player

class PlayerNotifications():
    def __init__(self, notifications: List[Notification], player: Player):
        self.notifications: List[Notification] = notifications
        self.is_empty: bool = len(self.notifications) == 0
        self.latest_notif_id: int = player.latest_notif_id if self.is_empty else max(int(notif.notification_id) for notif in notifications)
