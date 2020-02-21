#!/usr/bin/env python

from lib.actions import BaseAction
from lib.utils import find_by_field


class SumoGetCollector(BaseAction):
    def run(self, collector_id=None, collector_name=None):
        self.logger.debug('Name: %s', collector_name)
        self.logger.debug('ID: %s', collector_id)

        if self._client is None:
            self.logger.debug('No Access ID or Key is configured. Please, configure.')
            return False, {}

        collectors = self._client.collectors(self._sumologic_collectors_limit)

        if collector_id is not None and collector_id > 0:
            c = find_by_field(collectors, 'id', collector_id, True)
        else:
            c = find_by_field(collectors, 'name', collector_name, True)

        if len(c) == 1:
            return True, c[0]
        else:
            return True, {}
