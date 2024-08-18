from injector import Module, provider, singleton
import boto3
import typing

from aws.illyriad_db_dao import IllyriadDBDao

class AWSModule(Module):

    # TODO: Move these types else so they can be accessed in other classes/modules
    PlayersTable = typing.NewType('PlayersTable', object)
    MetadataTable = typing.NewType('MetadataTable', object)
    Boto3Session = typing.NewType('Boto3Session', object)
    DynamoDBResource = typing.NewType('DynamoDBResource', object)

    @singleton
    @provider
    def provide_illyriad_db_dao(self, metadata_table: MetadataTable, players_table: PlayersTable) -> IllyriadDBDao:
        return IllyriadDBDao(metadata_table, players_table)

    @singleton
    @provider
    def provide_dynamodb_res(self, session: Boto3Session) -> DynamoDBResource:
        return session.resource('dynamodb', region_name='us-west-2')

    @singleton
    @provider
    def provide_boto3_session(self) -> Boto3Session:
        return boto3.Session(profile_name='IllyriadServiceUser')

    @singleton
    @provider
    def provide_metadata_table(self, dynamodb_res: DynamoDBResource, stage: str) -> MetadataTable:
        return dynamodb_res.Table(f'Illyriad-Metadata-{stage}')

    @singleton
    @provider
    def provide_players_table(self, dynamodb_res: DynamoDBResource, stage: str) -> PlayersTable:
        return dynamodb_res.Table(f'Illyriad-Player-{stage}')
