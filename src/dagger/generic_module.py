from injector import Module, provider, singleton

from aws.illyriad_db_dao import IllyriadDBDao
from cache.metadata_cache import MetadataCache
from cache.player_cache import PlayerCache
from illyriad.illyriad import Illyriad
from illyriad.xml_parser import XMLParser
from discord.discord import Discord
from processor.player_notification_processor import PlayerNotificationProcessor
from processor.notifications_processsor import NotificationsProcessor
from notification_channels.incoming_channel import IncomingChannel

class GenericModule(Module):
    @singleton
    @provider
    def provide_metadata_cache(self, illyriad_db_dao: IllyriadDBDao) -> MetadataCache:
        return MetadataCache(illyriad_db_dao)

    @singleton
    @provider
    def provide_player_cache(self, illyriad_db_dao: IllyriadDBDao) -> PlayerCache:
        return PlayerCache(illyriad_db_dao)

    @singleton
    @provider
    def provide_illyriad(self, xml_parser: XMLParser) -> Illyriad:
        return Illyriad(xml_parser)

    @singleton
    @provider
    def provide_xml_parser(self) -> XMLParser:
        return XMLParser()
    
    @singleton
    @provider
    def provide_discord(self) -> Discord:
        return Discord()

    @singleton
    @provider
    def provide_incoming_channel(self, discord: Discord, metadata_cache: MetadataCache) -> IncomingChannel:
        return IncomingChannel(discord, metadata_cache)
    
    @singleton
    @provider
    def provide_player_notification_processor(self, player_cache: PlayerCache,
                                              illyriad: Illyriad, incoming_channel: IncomingChannel) -> PlayerNotificationProcessor:
        return PlayerNotificationProcessor(player_cache, illyriad, incoming_channel)

    @singleton
    @provider
    def provide_notifications_processor(self, metadata_cache: MetadataCache, player_cache: PlayerCache,
                                        player_notification_processor: PlayerNotificationProcessor) -> NotificationsProcessor:
        return NotificationsProcessor(metadata_cache, player_cache, player_notification_processor)

