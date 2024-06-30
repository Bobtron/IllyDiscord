from injector import Injector

from dagger.aws_module import AWSModule
from dagger.generic_module import GenericModule
from processor.notifications_processsor import NotificationsProcessor

def main():
    # This is pseudocode for flow of logic
    # Initialize NotificationsProcessor
    # NotificationsProcessor will initially grab all players from the dynamodb
    # In a loop, first the notificatios will check if the update flag on dynamodb was set. if so will reload all players from dynamodb and reset update flag
    # Then will run the playerNotification processor per player
    # Player notification processor will get list of notifications from the illyriad object (and the xml parser)
    # Then in each notification 'channel' object it will filter the incoming notification for the relevant notifaciton types (or any other filtering needed)
    # Notification channel object will post the relevant notification to discord objet
    # Player object at the end of running each notification 'channel' object will update dynamodb with the latest notification id
    # Internally it will save/cache the last notification rather than fetch again from dynamodb
    # Back to start of loop

    # Notifications process has a metadatacache, playercache, playernotificationprocessor
    # metadatacache has a illydbdao
    # playercache has an illydbdao
    # playernotification processor has metadatacahe, playercache, illyriad, discord
    # illyriad has a xmlparser

    injector = Injector([AWSModule(), GenericModule()])

    notifications_processor = injector.get(NotificationsProcessor)

    notifications_processor.process_notifications()

if __name__ == '__main__':
    main()