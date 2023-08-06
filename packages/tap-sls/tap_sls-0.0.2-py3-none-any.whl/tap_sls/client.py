"""REST client handling, including tap-slsStream base class."""
import json
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable
import copy
import os
import time

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



from singer_sdk import Tap, Stream
from aliyun.log import *
import singer

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

REQUIRED_CONFIG_KEYS = [
]

state_file = 'state.json'


class SlsStream(Stream):
    """tap-sls stream class."""

    def __init__(self, tap: Tap):
        super().__init__(tap=tap, name=None, schema=None)
        endpoint = self.config.get('endpoint')
        access_key_id = self.config.get('access_key_id')
        access_key = self.config.get('access_key')
        self.project = self.config.get('project')
        self.logstore = self.config.get('logstore')
        self.to_time = self.config.get('to_time')
        self.from_time = self.config.get('from_time')
        self.query = self.config.get('query')
        self.client = LogClient(endpoint, access_key_id, access_key)
        self._primary_keys=self.config.get('primary_keys')

    def get_logs(self, from_time, to_time, offset):
        if not self.query:
            self.query = ''
        request = GetLogsRequest(project=self.project, logstore=self.logstore,
                                 query=self.query,
                                 fromTime=from_time,
                                 toTime=to_time, topic='',
                                 offset=offset,
                                 reverse=False)
        response = self.client.get_logs(request)
        return response.get_count(), response.is_completed(), response.get_logs()


    @property
    def primary_keys(self):
        if not self._primary_keys:
            return []
        return self._primary_keys

    @primary_keys.setter
    def primary_keys(self, new_value: List[str]) -> None:
        self._primary_keys = new_value

    @staticmethod
    def get_record(log):
        items = log.contents.items()
        record = {}
        for item in items:
            record[item[0]] = item[1]
        return record

    def get_records(
            self, context: dict
    ) -> Iterable[dict]:
        state = self.get_context_state(context)
        from_time = singer.get_bookmark(state, self.tap_stream_id, 'to_time')
        if not from_time:
            from_time = self.from_time
        if not self.to_time:
            self.to_time = int(time.time())
        offset = 0

        log_count, is_completed, logs = self.get_logs(from_time, self.to_time, offset)

        for log in logs:
            record = self.get_record(log)
            yield record

        while log_count != 0 and is_completed:
            offset = offset + 100
            log_count, is_completed, logs = self.get_logs(from_time, self.to_time, offset)
            for log in logs:
                record = self.get_record(log)
                yield record

        state = singer.write_bookmark(state,
                                      self.tap_stream_id,
                                      'to_time', self.to_time
                                      )
        state = singer.write_bookmark(state,
                                      self.tap_stream_id,
                                      'from_time', self.from_time
                                      )
        singer.write_state(state)
