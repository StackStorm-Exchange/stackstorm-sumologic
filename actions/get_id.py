#!/usr/bin/env python

from lib.actions import BaseAction
import lib.utils


class SumoGetId(BaseAction):
    def run(self, keyword=None):
        self.logger.debug('keyword: %s', keyword)

        result = []
        if self._client is None:
            self.logger.debug('No Access ID or Key is configured. Please, configure.')
            return False, result

        collectors = self._client.collectors(self._sumologic_collectors_limit)
        c = lib.utils.find_by_field(collectors, 'name', keyword, False)
        return True, [d['id'] for d in c if 'id' in d]
