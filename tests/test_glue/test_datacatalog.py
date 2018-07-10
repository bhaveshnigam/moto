from __future__ import unicode_literals

import sure  # noqa
import boto3

from moto import mock_glue


def create_database(client, database_name):
    return client.create_database(
        DatabaseInput={
            'Name': database_name
        }
    )


def get_database(client, database_name):
    return client.get_database(Name=database_name)


@mock_glue
def test_create_database():
    client = boto3.client('glue', region_name='us-east-1')
    database_name = 'myspecialdatabase'
    create_database(client, database_name)

    response = get_database(client, database_name)
    database = response['Database']

    database.should.equal({'Name': database_name})
