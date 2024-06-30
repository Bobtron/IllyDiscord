import json

class Notification():
    # def __init__(
    #                 self,
    #                 notification_id: int,
    #                 notification_type_id: int,
    #                 notification_type: str,
    #                 notificationoveralltype_id: int,
    #                 notificationoveralltype: str,
    #                 notificationtown_id: int,
    #                 notificationdetail: str,
    #                 notificationoccurrencedate: str
    #             ):
    #     self.notification_id = notification_id
    #     self.notification_type_id = notification_type_id
    #     self.notification_type = notification_type
    #     self.notificationoveralltype_id = notificationoveralltype_id
    #     self.notificationoveralltype = notificationoveralltype
    #     self.notificationtown_id = notificationtown_id
    #     self.notificationdetail = notificationdetail
    #     self.notificationoccurrencedate = notificationoccurrencedate

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
        # return "null" if self.notif_obj is None else json.dumps(self.notif_obj, indent=2)
        return json.dumps(self.notif_obj, indent=2)
