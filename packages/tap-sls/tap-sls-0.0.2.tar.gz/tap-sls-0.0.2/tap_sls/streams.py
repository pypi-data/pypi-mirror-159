"""Stream type classes for tap-sls."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers


from singer_sdk import Tap, Stream
from tap_sls.client import SlsStream


from aliyun.log import LogClient

import logging

logger = logging.getLogger(__name__)

from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    IntegerType,
    NumberType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


# TODO: Delete this is if not using json files for schema definition
# SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class LogStream(SlsStream):
    """Define custom stream."""
    # primary_keys = ["time"]
    # replication_key = 'time'

    def __init__(self, tap: Tap):
        self.log_schema = None
        endpoint = tap.config.get('endpoint')
        access_key_id = tap.config.get('access_key_id')
        access_key = tap.config.get('access_key')
        self.project = tap.config.get('project')
        self.logstore = tap.config.get('logstore')
        self.to_time = tap.config.get('to_time')
        self.from_time = tap.config.get('from_time')
        self._primary_keys=tap.config.get('primary_keys')
        self.client = LogClient(endpoint, access_key_id, access_key)
        SlsStream.__init__(self, tap)


    @property
    def name(self):
        return self.project.replace('-','_')

    @property
    def schema(self):
        p = PropertiesList()
        if not self.log_schema:
            response = self.client.get_index_config(self.project, self.logstore)
            index_json = response.get_index_config().to_json()
            keys=index_json['keys']
            logger.info(type(keys))
            for k,v in keys.items():
                if v['type']=='long':
                    p.append(Property(k, NumberType))
                else:
                    p.append(Property(k, StringType))
            self.log_schema = p.to_dict()
        return self.log_schema
