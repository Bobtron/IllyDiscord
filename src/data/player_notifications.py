from typing import List

from data.notification import Notification

class PlayerNotifications():
    def __init__(self, notifications: List[Notification]):
        self.notifications: List[Notification] = notifications
        self.latest_notif_id: int = max(int(notif.notification_id) for notif in notifications)
        self.is_empty: bool = len(self.notifications) == 0