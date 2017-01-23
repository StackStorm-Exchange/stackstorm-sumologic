#!/usr/bin/env python

from lib.actions import BaseAction
from lib.mycollectors import MyCollectors


class SumoGetCollector(BaseAction):
    def run(self, collector_id=None, collector_name=None):
        self.logger.debug('Name: %s', collector_name)
        self.logger.debug('ID: %s', collector_id)

        if self._client is None:
            self.logger.debug('No Access ID or Key is configured. Please, configure.')
            return False, {}

        collector = MyCollectors(self._client)

        if collector_id is not None and collector_id > 0:
            c = collector.find_by_id(collector_id)
        else:
            c = collector.find(collector_name)

        if c is not None:
            return True, c
        else:
            return True, {}
