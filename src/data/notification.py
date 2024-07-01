import json

class Notification():
    def __init__(self, notif_obj):
        self.notif_obj = notif_obj
        self.notification_id            : str = notif_obj['notification_id']
        self.notificationtype_id        : str = notif_obj['notificationtype_id']
        self.notificationtype           : str = notif_obj['notificationtype']
        self.notificationoveralltype_id : str = notif_obj['notificationoveralltype_id']
        self.notificationoveralltype    : str = notif_obj['notificationoveralltype']
        self.notificationtown_id        : str = notif_obj['notificationtown_id']
        self.notificationdetail         : str = notif_obj['notificationdetail']
        self.notificationoccurrencedate : str = notif_obj['notificationoccurrencedate']

    def __str__(self):
        return json.dumps(self.notif_obj, indent=2)
    def __unicode__(self):
        return json.dumps(self.notif_obj, indent=2)
    def __repr__(self):
        return json.dumps(self.notif_obj, indent=2)
