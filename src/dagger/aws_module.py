from injector import Module, provider, singleton
import boto3
from mypy_boto3_dynamodb import DynamoDBServiceResource

from aws.illyriad_db_dao import IllyriadDBDao

class AWSModule(Module):
    @singleton
    @provider
    def provide_illyriad_db_dao(self, dynamodb_res: DynamoDBServiceResource) -> IllyriadDBDao:
        return IllyriadDBDao(dynamodb_res)

    @singleton
    @provider
    def provide_dynamodb_res(self) -> DynamoDBServiceResource:
        session = boto3.Session(profile_name='IllyriadServiceUser')
        return session.resource('dynamodb', region_name='us-west-2')
